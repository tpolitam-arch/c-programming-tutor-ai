# C Programming Tutor (with full notes)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpolitam-arch/c-programming-tutor-ai/blob/master/Run_C_Tutor_From_GitHub_with_notes.ipynb)

This project includes:
- Full Unit 1–5 notes in `notes/`
- A Colab-safe tutor app (`app/c_tutor_app.py`) using `microsoft/phi-3-mini-4k-instruct` by default
- Retrieval-only fallback if model cannot load in Colab Free

# C Programming Tutor - Free (Colab-ready)

This project is a free, Colab/Kaggle/HuggingFace-ready AI tutor for a C programming course.
It uses:
- sentence-transformers + FAISS for retrieval
- a small open-source instruct model from Hugging Face for generation
- Gradio for chat UI

## How to run (Google Colab)
1. Upload this project folder to Colab or clone the repo.
2. Install dependencies:
   !pip install -r requirements.txt
3. Run the app:
   !python app/c_tutor_app.py
4. Click the Gradio share link to open the tutor in your browser.

Note: If the LLM is too large for the free environment, replace MODEL in app/c_tutor_app.py with a smaller HF model or run in CPU mode.

