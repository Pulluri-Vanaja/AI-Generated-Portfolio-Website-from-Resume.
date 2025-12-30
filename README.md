# 🤖 AI-Generated-Portfolio-Website

AI Website Builder is an AI-powered application that allows users to generate complete frontend websites using a simple text prompt.
The app uses a Large Language Model (LLM) to generate HTML, CSS, and JavaScript, packages them into a ZIP file, and lets users download the website instantly.

[![Live App](https://img.shields.io/badge/Live%20App-Streamlit-red?style=for-the-badge&logo=streamlit)](https://ai-generated-portfolio-website-from-resume-x9cz3mxpl4gdzhyemsw.streamlit.app/)

🚀 What This App Does

1.User enters a short description of the website they want

The AI generates:

▫️index.html

▫️style.css

▫️script.js

2.All files are automatically combined into a ZIP file

3.User downloads the ZIP and can run the website locally

🎯 Key Features

🔹Generate frontend websites from natural language prompts

🔹Clean separation of HTML, CSS, and JavaScript

🔹No frameworks or external libraries used in generated code

🔹One-click ZIP file download

🔹Simple and beginner-friendly Streamlit UI

🔹Uses prompt engineering for structured AI output


🧠 How It Works

💠The user provides a website description

💠A strict system prompt forces the AI to output code in a fixed format

💠The app extracts HTML, CSS, and JS using simple string splitting

💠Files are written locally and zipped

💠The ZIP file is provided for download

🛠 Tech Stack
Frontend UI: Streamlit

LLM: Google Gemini

LLM Integration: LangChain

File Handling: Python zipfile

Secrets Management: .env file or Streamlit Cloud Secrets
