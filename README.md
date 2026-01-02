TechEase Product Support Assistant (RAG + Memory)

A LangChain-based Product Support Assistant for a fictional startup TechEase, built as a Mini RAG (Retrieval-Augmented Generation) system with conversational memory.

This assistant can:

Answer product questions using company documents

Remember short-term conversation context

Fall back safely when answers are not found in documents

🚀 Features

LLM-powered chat using Groq (LLaMA 3)

RAG pipeline with FAISS vector store

Document ingestion & chunking

Semantic search using embeddings

Conversation memory

Safe fallback handling

Modular, step-by-step project structure

🧠 Tech Stack

Python

LangChain

Groq (LLM)

FAISS (Vector Store)

Sentence Transformers (Embeddings)

dotenv

VS Code

📂 Project Structure
TeacherAssistant/
│
├── src/
│   ├── s01_llm_test.py            # Basic LLM test
│   ├── s02_chain_test.py          # Prompt + chain test
│   ├── s03_memory_test.py         # Conversational memory
│   ├── s04_load_doc.py            # Load documents
│   ├── s05_build_vectorStore.py   # Build FAISS vector store
│   └── s06_rag_chat.py            # Final RAG chatbot
│
├── data/
│   ├── docs/                      # Knowledge base documents
│   │   ├── refund_policy.txt
│   │   ├── pricing.txt
│   │   ├── integrations.txt
│   │   └── setup_guide.txt
│   └── vectorstore/               # FAISS index (auto-generated)
│
├── .env                           # API keys (NOT committed)
├── .gitignore
├── requirements.txt
└── README.md

📄 Knowledge Base Documents

The assistant answers questions using these documents:

Refund Policy

Pricing Plans

Integrations (Slack, Zapier, etc.)

Product Setup Guide

Documents are stored in:

data/docs/

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd TeacherAssistant

2️⃣ Create Virtual Environment
python -m venv .venv


Activate:

Windows

.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key_here


⚠️ Never upload .env to GitHub

▶️ How to Run the Project
Step 1: Load Documents
python src/s04_load_doc.py

Step 2: Build Vector Store
python src/s05_build_vectorStore.py

Step 3: Run RAG Chatbot
python src/s06_rag_chat.py

💬 Example Interaction
User: Do you offer refunds?
Assistant: Yes, TechEase offers a 14-day refund policy for new subscriptions.

User: Is there a free trial?
Assistant: A free trial may be available depending on promotions.

User: How do I set up TechEase?
Assistant: To get started, create an account, verify your email, configure settings, and connect integrations.

🛡️ Safety & Fallback

If no relevant document is found, the assistant responds with a safe fallback

Prevents hallucinated answers

Uses document-grounded responses only

🎯 Assignment Objectives Covered

✅ Conversational Memory
✅ Mini RAG Implementation
✅ Document Retrieval with Embeddings
✅ Modular LangChain Design
✅ Working End-to-End Assistant


👩‍💻 Author

Hira Barlas
Aspiring Data & AI Analyst
UAE
