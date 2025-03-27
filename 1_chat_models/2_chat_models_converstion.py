from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

messages = [
  SystemMessage("You are an expert in social media content strategy"),
  HumanMessage("Give a short tip to create engaging posts on Instagram")
]

result = llm.invoke(messages)

print(result.content)