from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["user_input"],
    template=(
        "You are TechEase Support Assistant.\n"
        "Answer the user clearly and briefly.\n\n"
        "User: {user_input}\n"
        "Assistant:"
    )
)

chain = prompt | llm

while True:
    user_text = input("User: ").strip()
    if user_text.lower() in ("exit", "quit"):
        print("Assistant: Goodbye!")
        break

    response = chain.predict(user_input=user_text)
    print("Assistant:", response, "\n")
