import os
import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load notes
docs, metas = [], []
for root, _, files in os.walk("notes"):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as fh:
                text = fh.read()
            docs.append(text)
            metas.append(path)

# Build embeddings and FAISS index
embedder = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = embedder.encode(docs, convert_to_numpy=True)
d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

def retrieve(query, k=2):
    qv = embedder.encode([query], convert_to_numpy=True)
    D, I = index.search(qv, k)
    return [docs[i] for i in I[0]]

# LLM (default small model)
MODEL = "microsoft/phi-3-mini-4k-instruct"
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL)
gen = pipeline("text-generation", model=model, tokenizer=tok)

def answer(user_input, history):
    context = "\n\n".join(retrieve(user_input, k=3))
    prompt = f"""You are a friendly C programming tutor for first-year B.Tech students.
Use the context below when relevant. Cite the source path when you reference specific facts.

CONTEXT:
{context}

STUDENT:
{user_input}

TUTOR:
"""
    out = gen(prompt, max_new_tokens=200, temperature=0.6)[0]["generated_text"]
    if "TUTOR:" in out:
        ans = out.split("TUTOR:")[-1].strip()
    elif "Tutor:" in out:
        ans = out.split("Tutor:")[-1].strip()
    else:
        ans = out
    history = history or []
    history.append((user_input, ans))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# 🎓 C Programming Tutor (Free)")
    chatbot = gr.Chatbot()
    txt = gr.Textbox(placeholder="Ask a C programming question...", show_label=False)
    txt.submit(answer, [txt, chatbot], [chatbot, chatbot])
    gr.Button("Clear").click(lambda: None, None, chatbot)

if __name__ == '__main__':
    demo.launch(share=True)
