import streamlit as st
import os
import zipfile
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from PyPDF2 import PdfReader
import docx

# Load environment variables
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# Streamlit config
st.set_page_config(page_title="AI Resume to Portfolio", layout="wide")
st.title("AI-Generated Portfolio Website from Resume")

# Resume Text Extractor
def extract_resume_text(uploaded_file):
    text = ""

    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text



# Upload Resume
uploaded_resume = st.file_uploader(
    "Upload your Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

generate_btn = st.button("Generate Portfolio Website")

if uploaded_resume and generate_btn:

    resume_text = extract_resume_text(uploaded_resume)

    if len(resume_text.strip()) == 0:
        st.error("Could not extract text from resume.")
        st.stop()


    messages = [
        ("system", """
You are a SENIOR FRONTEND ENGINEER and UI DESIGNER.

TASK:
Generate a PROFESSIONAL, MODERN, LINKEDIN-STYLE PORTFOLIO WEBSITE
from the resume content provided.

STRICT DESIGN RULES:
- Modern layout (LinkedIn / Portfolio quality)
- Use Flexbox & CSS Grid
- Cards, shadows, spacing, rounded corners
- Clean color palette & modern fonts
- Fully responsive design
- NO documentation, ONLY WEBSITE CODE
- HTML MUST LINK CSS & JS PROPERLY

OUTPUT FORMAT (MANDATORY):

--html--
[Complete index.html]
--html--

--css--
[Complete style.css]
--css--

--js--
[Optional script.js]
--js--
""")
    ]

    messages.append(("user", resume_text))

    # LLM Call
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response = model.invoke(messages)

   
    # Extract Files
    html = response.content.split("--html--")[1].strip()
    css = response.content.split("--css--")[1].strip()
    js = response.content.split("--js--")[1].strip()

    
    # Save Files
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css)

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js)

    
    # ZIP Export
    with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    st.success("✅ Portfolio website generated successfully!")

    st.download_button(
        label="⬇️ Download Website ZIP",
        data=open("portfolio_website.zip", "rb"),
        file_name="portfolio_website.zip",
        mime="application/zip"
    )
