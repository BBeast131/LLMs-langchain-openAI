from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# load environment variables from .env file
load_dotenv()

# Create a ChatOpenAI model
model = ChatGroq(model="llama-3.3-70b-versatile")

chat_history = [] # Use a list to store messages

# Set an initial system message
system_message = SystemMessage("You are a helpful AI assistant.")
chat_history.append(system_message) # Add system message to chat history

# Chat roop
while True:
  query = input("User: ")
  if query.lower() == "exit":
    break
  chat_history.append(HumanMessage(query)) # Add user message to chat history

  result = model.invoke(chat_history) # Pass the entire chat history to the model 
  response = result.content
  chat_history.append(AIMessage(response)) # Add model response to chat history
  
  print(f"AI:{response}")

print("----------Message History----------")
print(chat_history) # Print the entire chat history