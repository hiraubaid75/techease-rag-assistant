from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template=(
        "You are TechEase Product Support Assistant.\n"
        "You MUST remember user details shared earlier (like their name) and use chat history.\n\n"
        "Chat history:\n{chat_history}\n\n"
        "User: {user_input}\n"
        "Assistant:"
    )
)

chat_history = ""  # simple session memory stored in this variable

print("Memory Bot running. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ").strip()
    if user_input.lower() in ("exit", "quit"):
        print("Assistant: Goodbye!")
        break

    # Build messages using prompt + history
    formatted = prompt.format(chat_history=chat_history, user_input=user_input)

    response = llm.invoke(formatted)
    answer = response.content

    print("Assistant:", answer, "\n")

    # Update history (this is your short-term memory)
    chat_history += f"User: {user_input}\nAssistant: {answer}\n"
