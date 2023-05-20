import streamlit as st
import os
from langchain import OpenAI

st.title('🦜🔗 Quickstart App')

if 'OPENAI_API_KEY' in st.secrets:
  st.success('Key is provided!', icon='🔑')
  os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

def generate_response(input_text):
  llm = OpenAI(temperature=0.7)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are 3 key advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if submitted:
    generate_response(text)
