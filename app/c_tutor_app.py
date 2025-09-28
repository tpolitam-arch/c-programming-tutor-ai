# app/c_tutor_app.py
import os
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# ========== Load notes ==========
docs, metas = [], []
for root, _, files in os.walk("notes"):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            docs.append(text)
            metas.append(path)

# ======= Embedding Index (FAISS) =======
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(docs, convert_to_numpy=True)
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

def retrieve(query, k=3):
    qv = embedder.encode([query], convert_to_numpy=True)
    D, I = index.search(qv, k)
    results = []
    for idx in I[0]:
        if idx < len(docs):
            results.append(docs[idx])
    return results

# ======= LLM Model (safer defaults + env override) =======
# Default model chosen to be Colab-friendly. You can override by setting environment variable C_TUTOR_MODEL.
MODEL = os.environ.get('C_TUTOR_MODEL','microsoft/phi-3-mini-4k-instruct')


# Lazy load with safe fallback
tok = None
model = None
gen = None
model_loaded = False

try:
    # Attempt to load tokenizer & model
    tok = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForCausalLM.from_pretrained(MODEL)
    gen = pipeline("text-generation", model=model, tokenizer=tok)
    model_loaded = True
    print(f"Loaded model: {MODEL}")
except Exception as e:
    print(f"Warning: failed to load model '{MODEL}': {e}")
    print("Falling back to retrieval-only responses (the tutor will answer using course notes).")
    tok = None
    model = None
    gen = None
    model_loaded = False

# ======= Answer function with fallback =======
def answer(user_input, history):
    history = history or []
    context_chunks = retrieve(user_input, k=3)
    context = "\n\n".join([f"[SOURCE {i+1}]\n{c}" for i, c in enumerate(context_chunks)]) if context_chunks else ""
    prompt = f"You are a friendly C programming tutor for first-year B.Tech students.\n\nContext:\n{context}\n\nStudent: {user_input}\nTutor:"
    ans = None

    if model_loaded and gen is not None:
        try:
            out = gen(prompt, max_new_tokens=200, temperature=0.6)[0]["generated_text"]
            # try extracting the tutor portion if present
            if "TUTOR:" in out:
                ans = out.split("TUTOR:")[-1].strip()
            elif "Tutor:" in out:
                ans = out.split("Tutor:")[-1].strip()
            else:
                # model might echo entire prompt + output; remove prompt if present
                ans = out.replace(prompt, "").strip()
        except Exception as e:
            print(f"Model generation failed: {e} -- falling back to retrieval-only.")
            ans = None

    # Retrieval-only fallback
    if not ans:
        if context:
            ans = "Based on course notes (retrieval fallback):\n\n" + context
        else:
            ans = "I don't have notes for that topic yet. Add notes into the `notes/` folder to improve answers."

    history.append((user_input, ans))
    return history, history

# ======= Gradio UI =======
with gr.Blocks() as demo:
    gr.Markdown("# 🎓 C Programming Tutor (Free)\nThis tutor uses course notes and a small open-source model. If a large model fails to load, the tutor will answer using retrieval from the notes.")
    chatbot = gr.Chatbot()
    txt = gr.Textbox(placeholder="Ask a C programming question...", show_label=False)
    txt.submit(answer, [txt, chatbot], [chatbot, chatbot])
    gr.Button("Clear").click(lambda: None, None, chatbot)

if __name__ == "__main__":
    demo.launch(share=True)
