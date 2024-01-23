import os
from dotenv import load_dotenv
import google.generativeai as genai
import json
import PyPDF2 as pdf
from src.logger import logging



def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    logging.info('reading pdf')
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        logging.info(page)
        text += str(page.extract_text())
    return text