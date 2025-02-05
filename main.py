import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("SECRET_KEY"))

# Initialize Generative Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a friendly and helpful AI assistant.",
)

# Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    response = model.generate_content(contents=user_input)
    ai_response = response.text

    # Append AI message
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)
