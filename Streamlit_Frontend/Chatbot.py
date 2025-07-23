import streamlit as st
import requests

# ✅ Must come first before any other Streamlit commands
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
)

st.title("🍽️ Chat with DietBot")

# Input box for user's message
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    try:
        # ✅ Use container name instead of localhost for Docker networking
        response = requests.post("http://backend:8080/chat/", json={"message": user_input})
        
        if response.ok:
            reply = response.json().get("reply", "🤖 No reply received.")
            st.text_area("DietBot:", reply, height=100)
        else:
            st.error("⚠️ Server responded with an error. Please check backend logs.")
    except requests.exceptions.RequestException as e:
        st.error("❌ Could not connect to the chatbot server.")
        st.info(f"Details: {e}")
