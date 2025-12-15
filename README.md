🚀 AI-Powered Portfolio Website Generator

An end-to-end AI application that automatically generates a professional, multi-section portfolio website from a user’s resume (PDF/DOCX) or text prompt.
The system produces production-ready HTML, CSS, and JavaScript, bundles everything into a deployable ZIP file, and provides a live preview — all through an intuitive Streamlit interface.

📌 Problem Statement

Creating a personal portfolio website requires frontend skills, design effort, and time.
Many students, freshers, and professionals struggle to quickly build a polished online presence.

Goal:
Automate portfolio website creation using AI and Python, requiring zero frontend coding knowledge from the user.

💡 Solution Overview

This project implements a complete AI-driven pipeline:

Resume upload (PDF or DOCX)

Intelligent text extraction

Structured data generation using LLMs

Frontend website code generation (HTML/CSS/JS)

Live preview inside the app

One-click ZIP download for deployment

🛠️ Tech Stack
Layer	Technology
UI	Streamlit
Resume Parsing	PyPDF2, python-docx
LLM Orchestration	LangChain
LLM Model	Google Gemini
Backend & Automation	Python
File Packaging	zipfile
🔄 Workflow

Resume Upload
Users upload a PDF or DOCX resume via Streamlit.

Text Extraction

PDFs: PyPDF2

DOCX: python-docx

Prompt Engineering (LLM #1)
Resume text is converted into a structured website specification (name, skills, experience, projects, education).

Code Generation (LLM #2)
Google Gemini generates clean, semantic HTML, CSS, and JavaScript.

Preview & Download
The website is rendered inside Streamlit and packaged as a ZIP file for deployment.

✨ Key Features

✅ Fully automated portfolio generation

✅ Supports PDF and DOCX resumes

✅ Clean, production-ready frontend code

✅ Live website preview

✅ One-click ZIP download

✅ Beginner-friendly UI
