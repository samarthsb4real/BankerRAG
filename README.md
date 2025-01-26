# RAG-Based Investment Banking Chatbot (BankerRAG)

### Setup Instructions:
1. Install Required Packages
  ```bash
  pip install flask fastapi langchain langchain_community langchain_huggingface langchain_core langchain_chroma
  ```
2. Download the LLM Model (neural-chat-7b-v3-1.Q4_K_M.gguf):
  ```
  https://huggingface.co/TheBloke/neural-chat-7B-v3-1-GGUF/blob/main/neural-chat-7b-v3-1.Q4_K_M.gguf
  ```
3. Initialize Vectorstore and generate pet_cosine for Data:
  ```
  python ingest.py
  ```
4. Run the Model
  ```
  python flask_app.py
  ```

### To-do list
1. Gather more IB related data
2. UI Design, more GPT-like interface
3. Fine tuning this / trying alternate LLM models
5. Optimize the error handling
