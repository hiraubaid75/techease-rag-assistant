from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_txt_documents(docs_dir: str):
    docs_path = Path(docs_dir)
    txt_files = sorted(docs_path.glob("*.txt"))

    if not txt_files:
        raise FileNotFoundError(f"No .txt files found in: {docs_path.resolve()}")

    documents = []
    for f in txt_files:
        loader = TextLoader(str(f), encoding="utf-8")
        documents.extend(loader.load())
    return documents


def split_into_chunks(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=80)
    return splitter.split_documents(documents)


if __name__ == "__main__":
    docs_dir = r"data\docs"

    docs = load_txt_documents(docs_dir)
    chunks = split_into_chunks(docs)

    # Local embeddings (no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build FAISS index
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save locally
    out_dir = Path("data/vectorstore")
    out_dir.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(out_dir))

    print("✅ Vector store created and saved!")
    print(f"Documents: {len(docs)} | Chunks: {len(chunks)}")
    print(f"Saved to: {out_dir.resolve()}")


