import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

## Configure API Key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## Prompt Template

input_prompt =f"""
You are a skilled in ATS(Application Tracking System).
You are a expert in technical field, software engineering, \
data science and data analyst.




"""



