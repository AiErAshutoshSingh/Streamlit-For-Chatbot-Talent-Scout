import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# ===============================
# 🔧 SETUP
# ===============================
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🧠",
    layout="wide",
)

# ===============================
# 🎨 CUSTOM CSS STYLING
# ===============================
st.markdown("""
<style>
body {
    background-color: #f5f6fa;
}
.chat-container {
    max-width: 780px;
    margin: auto;
}
.user-bubble, .assistant-bubble {
    padding: 0.9em 1.1em;
    border-radius: 16px;
    margin-bottom: 0.8em;
    width: fit-content;
    max-width: 80%;
    line-height: 1.5em;
}
.user-bubble {
    background-color: #0078d7;
    color: white;
    margin-left: auto;
}
.assistant-bubble {
    background-color: #ffffff;
    color: #222;
    border: 1px solid #ddd;
}
.avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    margin-right: 8px;
    vertical-align: middle;
}
.chat-row {
    display: flex;
    align-items: flex-start;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# 🧠 SIDEBAR INFO
# ===============================
st.sidebar.title("🧭 TalentScout Assistant")
st.sidebar.markdown("""
Welcome to TalentScout, your AI-powered hiring assistant!  

💼 **Features**
- Gathers candidate details (name, email, experience, etc.)
- Understands your **tech stack**
- Generates **tailored technical questions**
- Maintains context & ends gracefully  

Type `exit`, `bye`, or `quit` to finish.  
""")

# ===============================
# 📜 SESSION MANAGEMENT
# ===============================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """
You are TalentScout, an intelligent hiring assistant for a tech recruitment agency.
Your role:
1. Greet the user and explain your purpose.
2. Collect:
   - Full name
   - Email address
   - Phone number
   - Years of experience
   - Desired position(s)
   - Current location
   - Tech stack (languages, frameworks, tools)
3. Based on the tech stack, generate 3–5 relevant technical questions.
4. Stay professional, friendly, and context-aware.
5. If user says bye/exit/quit, end conversation politely.
        """},
        {"role": "assistant", "content": "Hello 👋! I’m **TalentScout**, your AI hiring assistant. Let’s get started — may I have your **full name**?"}
    ]

# ===============================
# 💬 DISPLAY CHAT
# ===============================
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.markdown(f"""
        <div class="chat-row">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="avatar"/>
            <div class="assistant-bubble">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    elif msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-row" style="justify-content: flex-end;">
            <div class="user-bubble">{msg["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 📝 USER INPUT
# ===============================
if prompt := st.chat_input("Type your response here..."):
    # Display user message
    st.markdown(f"""
    <div class="chat-row" style="justify-content: flex-end;">
        <div class="user-bubble">{prompt}</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Exit condition
    if any(word in prompt.lower() for word in ["bye", "exit", "quit", "end"]):
        farewell = "Thank you for chatting with TalentScout! We'll review your information and contact you soon. 👋"
        st.markdown(f"""
        <div class="chat-row">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="avatar"/>
            <div class="assistant-bubble">{farewell}</div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": farewell})
        st.stop()

    # ===============================
    # 🧩 CALL GROQ LLM
    # ===============================
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            temperature=0.7,
        )

        reply = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": reply})

        st.markdown(f"""
        <div class="chat-row">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="avatar"/>
            <div class="assistant-bubble">{reply}</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
