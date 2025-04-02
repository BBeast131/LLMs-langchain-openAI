from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_chatanthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


messages = [
  SystemMessage("You are an expert in social media content strategy"),
  HumanMessage("Give a short tip to create engaging posts on Instagram")
]

llm = ChatGroq(model="llama-3.3-70b-versatile")

result = llm.invoke(messages)

print("answer from genai", result.content)
print("\n")

llm = ChatAnthropic(model_name="claude-3-opus-20240229")
result = llm.invoke(messages)
print("Answer from Anthropic:",result.content)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
result = llm.invoke(messages)
print("Answer from google",result.content)