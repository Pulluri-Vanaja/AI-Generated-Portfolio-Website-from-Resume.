import streamlit as st
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
import zipfile

os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="AI website creation")

st.title("AI AUTOMATION WEBSITE CREATION")

prompt = st.text_area("write here about your website")

if st.button("generate"):
    message = [("system","""You are an expert frontend engineer who creates modern, beautiful, production-quality UIs.
                IMPORTANT RULES (must always be followed):
                1. ALWAYS use TAILWIND CSS classes inside HTML. 
                2. Do NOT write plain/minimal CSS. 
                3. Do NOT output ugly, basic, default HTML.
                4. ALWAYS create a complete, modern, responsive UI with:
                - Flexbox
                - Grid
                - Spacing (p-4, m-4, gap-4)
                - Rounded corners
                - Shadow
                - Professional color palette
                - Clean typography
                5. Your websites MUST look like real websites (LinkedIn, Facebook, Instagram, dashboards, etc.)
                6. NEVER output minimal/unstyled layouts.

                OUTPUT FORMAT (strict):
                --html--
                [Full HTML with Tailwind CDN + responsive layout]
                --html--

                --css--
                /* Only extra custom CSS if needed. Keep small. */
                --css--

                --js--
                [JS for interactions if needed]
               --js--

               If the user describes a website, you MUST generate a polished, professional-looking UI using Tailwind.
               """
                )]



    message.append(("user", prompt))

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response = model.invoke(message)

    
    # with open("page.html","w")as file:
    #     file.write(response.content.split("--html--")[1])

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.content.split("--html--")[1].split("---html---")[0].strip())

    with open("style.css", "w", encoding="utf-8") as file:
        file.write(response.content.split("--css--")[1].split("---css---")[0].strip())

    with open("script.js", "w", encoding="utf-8") as file:
        file.write(response.content.split("--js--")[1].split("---html---")[0].strip())



    # with open("page.css","w")as file:
    #     file.write(response.content.split("--css--")[1])

    # with open("page.js","w")as file:
    #     file.write(response.content.split("--js--")[1])
   
    with zipfile.ZipFile("website.zip","w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    st.download_button(
        "Click to download website",
        data=open("website.zip", "rb"),
        file_name="website.zip"
    )

    st.success("Website generated successfully!")
