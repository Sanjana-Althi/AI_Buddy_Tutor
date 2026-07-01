import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Learning Buddy - Sanjana",
    page_icon="🎓",
    layout="centered"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🎓 AI Learning Buddy")
    st.markdown("---")
    st.markdown("""
### 👩‍💻 About

This AI Learning Buddy helps students learn **EASILY** through:

- 📖 Concept Explanations
- 🌍 Real-Life Examples
- 📝 Quiz Generation
- 💬 Ask Anything

---
**Developed by:**  
**Althi Sanjana**

**Capstone Project**  
Infosys Springboard AI EMPOW(H)ER Program
""")

# ---------------- Main Page ----------------
st.title("🎓 AI Learning Buddy - Sanjana")

st.markdown(
    """
Welcome! 👋

I'm **Sanjana**, your AI Study Buddy.

Choose an activity below, enter a topic, and I'll help you learn in a simple and interactive way.
"""
)

st.divider()

topic = st.text_input(
    "📚 Enter a Topic",
    placeholder="Example: Artificial Intelligence, SQL, Python..."
)

option = st.selectbox(
    "🎯 Choose Activity",
    [
        "📖 Explain Concept",
        "🌍 Real-Life Example",
        "📝 Generate Quiz",
        "💬 Ask Anything"
    ]
)

if st.button("🚀 Generate Response", use_container_width=True):

    if topic.strip() == "":
        st.warning("⚠️ Please enter a topic.")
    else:

        if option == "📖 Explain Concept":
            prompt = f"""
You are Sanjana, a friendly AI Study Buddy specializing in Data Analytics.

Explain {topic} in simple language for a beginner.

Include:
- Easy explanation
- One real-life example
- Why it is important
- Short summary
"""

        elif option == "🌍 Real-Life Example":
            prompt = f"""
You are Sanjana, an AI Study Buddy.

Give one simple real-life example of {topic} and explain it in beginner-friendly language.
"""

        elif option == "📝 Generate Quiz":
            prompt = f"""
You are Sanjana, an AI Study Buddy.

Create 5 multiple-choice questions on {topic}.

Each question should contain:
- Four options (A, B, C, D)
- Correct answer
- Short explanation
"""

        else:
            prompt = topic

        with st.spinner("🤖 Sanjana is generating your response..."):

            response = model.generate_content(prompt)

        st.divider()

        st.subheader("✨ AI Response")

        st.info(response.text)

st.divider()

st.caption(
    "🎓 Built by Althi Sanjana | Capstone Project | Infosys Springboard AI EMPOW(H)ER Program"
)
