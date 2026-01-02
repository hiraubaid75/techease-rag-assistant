from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


FALLBACK_MSG = "I couldn’t find this information in the available documents."


def build_llm():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


def load_vectorstore():
    # IMPORTANT: Use the same embedding model you used when building the index
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vs = FAISS.load_local("data/vectorstore", embeddings, allow_dangerous_deserialization=True)
    return vs


def format_prompt(question: str, context: str) -> str:
    return f"""
You are TechEase Product Support Assistant.

You MUST answer ONLY using the provided CONTEXT from internal documents.
If the answer is not clearly present in the CONTEXT, reply exactly with:
{FALLBACK_MSG}

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
""".strip()


if __name__ == "__main__":
    llm = build_llm()
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    print("RAG Bot running (TechEase docs). Type 'exit' to quit.\n")

    while True:
        question = input("User: ").strip()
        if question.lower() in ("exit", "quit"):
            print("Assistant: Goodbye!")
            break

        docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in docs]).strip()

        # If retrieval returns nothing meaningful, force fallback
        if not context or len(context) < 20:
            print("Assistant:", FALLBACK_MSG, "\n")
            continue

        prompt = format_prompt(question, context)
        response = llm.invoke(prompt)
        answer = response.content.strip()

        # Safety check: if model ignores instruction, enforce fallback
        if (FALLBACK_MSG.lower() not in answer.lower()) and (answer == "" or len(answer) < 3):
            answer = FALLBACK_MSG

        print("Assistant:", answer, "\n")
