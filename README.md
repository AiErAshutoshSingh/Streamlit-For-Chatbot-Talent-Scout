# 🧠 TalentScout Hiring Assistant

TalentScout is an **AI-powered recruitment assistant** built with **Streamlit** and **Groq’s LLM API**.  
It automates candidate pre-screening by collecting essential information and generating **tailored technical interview questions** based on the applicant’s tech stack.

---

## 🚀 Features

- 🧾 Collects candidate details:
  - Full Name  
  - Email Address  
  - Phone Number  
  - Years of Experience  
  - Desired Position(s)  
  - Current Location  
  - Tech Stack (Languages, Frameworks, Tools)
- 🤖 Powered by **Groq’s Llama 3.3 (70B)** model for contextual and intelligent conversations  
- 🎯 Generates **3–5 technical questions** based on the candidate’s experience  
- 💬 Professional, user-friendly **chat interface** with modern design  
- 🪄 Handles polite exit commands (`bye`, `exit`, `quit`) gracefully  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Groq Llama 3.3 70B |
| Environment Management | python-dotenv |
| Styling | Custom HTML/CSS |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/talentscout-assistant.git
cd talentscout-assistant



2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # (On Windows: venv\Scripts\activate)

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run app.py


💻 Usage

Once the app is running locally:

Open the Streamlit URL shown in your terminal (default: http://localhost:8501)
Chat with TalentScout:
Introduce yourself
Provide your details
See automatically generated interview questions
Type bye, exit, or quit to end the conversation politely.

