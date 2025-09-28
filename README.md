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

