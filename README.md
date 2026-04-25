# 🤖 DocuMind AI — Intelligent Document Chatbot

> Upload any document. Ask anything. Get instant, accurate answers powered by GPT-4o.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📌 Overview

**DocuMind AI** is a Retrieval-Augmented Generation (RAG) chatbot that lets you have a natural conversation with any document. Upload a PDF, Word file, or text document and ask questions in plain English — the AI reads, understands, and responds with precise, context-aware answers drawn directly from your file.

No hallucinations. No guessing. Only answers grounded in your document.

---

## ✨ Features

- 📄 **Multi-format Document Support** — Upload PDFs, DOCX, TXT, and more
- 🧠 **RAG Architecture** — Retrieves only the most relevant document chunks before answering
- 💬 **Conversational Memory** — Maintains context across follow-up questions in the same session
- ⚡ **GPT-4o Powered** — Uses OpenAI's latest and most capable model for responses
- 🖥️ **Intuitive Web UI** — Clean, browser-based interface built with Streamlit
- 🔒 **Local Processing** — Your documents are processed locally and never stored permanently

---

## 🏗️ Architecture

```
User Uploads Document
        │
        ▼
┌───────────────────┐
│  Document Loader  │  ← PyPDF2 / python-docx
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Text Chunker     │  ← LangChain RecursiveCharacterTextSplitter
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Vector Embeddings│  ← OpenAI text-embedding-ada-002
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Vector Store     │  ← FAISS / ChromaDB
└────────┬──────────┘
         │
    User asks a question
         │
         ▼
┌───────────────────┐     ┌──────────────────┐
│  Retriever        │────▶│  GPT-4o (OpenAI) │
└───────────────────┘     └────────┬─────────┘
                                   │
                                   ▼
                          Answer displayed in UI
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/documind-ai.git
cd documind-ai
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up your environment variables**

```bash
cp .env.example .env
```

Open `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

**5. Run the app**

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 🧪 Usage

1. **Launch** the app using the command above
2. **Upload** your document using the sidebar file uploader (PDF, DOCX, or TXT)
3. **Wait** for the document to be processed and indexed (takes a few seconds)
4. **Ask** any question in the chat input at the bottom
5. **Receive** an AI-generated answer sourced directly from your document

---

## 📁 Project Structure

```
documind-ai/
│
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore
├── README.md
│
├── src/
│   ├── document_loader.py  # Handles file ingestion and parsing
│   ├── chunker.py          # Text splitting logic
│   ├── embeddings.py       # Vector embedding generation
│   ├── vector_store.py     # FAISS/ChromaDB vector store management
│   ├── retriever.py        # Semantic search and chunk retrieval
│   └── chatbot.py          # LangChain RAG chain and GPT-4o integration
│
└── utils/
    └── helpers.py          # Shared utility functions
```

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| **LLM** | OpenAI GPT-4o |
| **Embeddings** | OpenAI text-embedding-ada-002 |
| **RAG Framework** | LangChain |
| **Vector Store** | FAISS / ChromaDB |
| **Web UI** | Streamlit |
| **Document Parsing** | PyPDF2, python-docx, LangChain loaders |
| **Language** | Python 3.10+ |

---

## ⚙️ Configuration

You can tweak the following settings in `.env` or directly in `src/`:

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | Your OpenAI API key (required) |
| `CHUNK_SIZE` | `1000` | Number of characters per document chunk |
| `CHUNK_OVERLAP` | `200` | Overlap between consecutive chunks |
| `TOP_K_RESULTS` | `4` | Number of chunks retrieved per query |
| `MODEL_NAME` | `gpt-4o` | OpenAI model to use for generation |

---

## 🛣️ Roadmap

- [ ] Support for multi-document uploads in a single session
- [ ] Chat history export (PDF / Markdown)
- [ ] User authentication and session persistence
- [ ] Support for URLs and web scraping as input
- [ ] Streaming responses for faster perceived performance
- [ ] Integration with Google Drive / OneDrive

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please make sure your code follows the existing style and includes relevant tests where applicable.

---

## 🙏 Acknowledgements

- [OpenAI](https://openai.com) for GPT-4o and the Embeddings API
- [LangChain](https://langchain.com) for the RAG orchestration framework
- [Streamlit](https://streamlit.io) for making Python web apps effortless
- [FAISS](https://github.com/facebookresearch/faiss) by Meta AI for fast vector search

---

<div align="center">

Made with ❤️ by [Your Name](https://github.com/GM45)

⭐ Star this repo if you found it helpful!

</div>
