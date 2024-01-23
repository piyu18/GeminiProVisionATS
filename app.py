import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from src.logger import logging
import json
import PyPDF2 as pdf
from src.utils import get_gemini_response, input_pdf_text

load_dotenv()

## Configure API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## Prompt Template

input_prompt ="""
You are a skilled in ATS(Application Tracking System).
You are a expert in technical field, software engineering, 
data science and data analyst. Your task is to evaluate the resume
based on the given JD(Job Description). You should consider that the job market is
very competitive and you should  provide the best assistance for improving the resumes.
Assign the percentage matching based on the JD and the missing key words with high accuracy.
resume: {text}
description: {JD}
I want the response in one single string having the structure {{"JD Match": "%", "MissingKeywords: []", "Profile Summary": ""}}



"""


st.title('ATS- GeminiPro')
st.text('Improve your Resume')

JD = st.text_area('Paste the Job Description')
uploaded_file = st.file_uploader("Upload your Resume", type="pdf", help="Please uploade the PDF")

submit = st.button('Submit')

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)
