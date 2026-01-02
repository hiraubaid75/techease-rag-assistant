from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_txt_documents(docs_dir: str):
    """Load all .txt files from data/docs into LangChain Document objects."""
    docs_path = Path(docs_dir)
    txt_files = sorted(docs_path.glob("*.txt"))

    if not txt_files:
        raise FileNotFoundError(f"No .txt files found in: {docs_path.resolve()}")

    documents = []
    for f in txt_files:
        # Keep encoding explicit to avoid Windows encoding issues
        loader = TextLoader(str(f), encoding="utf-8")
        documents.extend(loader.load())

    return documents


def split_into_chunks(documents):
    """Split documents into smaller chunks for retrieval."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80
    )
    return splitter.split_documents(documents)


if __name__ == "__main__":
    docs_dir = r"data\docs"  # your folder name
    docs = load_txt_documents(docs_dir)
    chunks = split_into_chunks(docs)

    print(f"Loaded documents: {len(docs)}")
    print(f"Total chunks: {len(chunks)}\n")

    # Show a few chunks so you can screenshot this for deliverables
    for i, c in enumerate(chunks[:5], start=1):
        source = c.metadata.get("source", "unknown")
        preview = c.page_content[:200].replace("\n", " ")
        print(f"[Chunk {i}] source={source}")
        print(preview)
        print("-" * 60)
