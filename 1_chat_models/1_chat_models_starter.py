from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile")

result = llm.invoke("what is the square root of 49?")

print(result.content)