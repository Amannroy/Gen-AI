from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Page Setup
st.title("Ask Buddy AI Q&A Bot 🤖")
st.markdown("My Q&A Bot with LangChain and Google Gemini")

# Initialize chat history(st.session_state used by streamlit to remember data between reruns of the app)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)    

# Get new question
query = st.chat_input("Ask Anythng...")

# Process new question
if query:
    # Show user's question immediately
    st.chat_message("user").markdown(query)

    # Save to history
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    # Get AI response
    response = llm.invoke(query)

    # Show AI's answer
    st.chat_message("ai").markdown(response.content)

    # Save to history
    st.session_state.messages.append({
        "role": "ai",
        "content": response.content
    })
