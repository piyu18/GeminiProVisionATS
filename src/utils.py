import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import PyPDF2 as pdf


load_dotenv()

## Configure API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini_pro')
    response = model.generate_content(input)
    return json.loads(response)


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text