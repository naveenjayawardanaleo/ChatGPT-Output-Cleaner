import streamlit as st
import re

def clean_text(text):
    def clean_line(line):
        line = re.sub(r'^#+\s*', '', line)
        line = re.sub(r'\*+', '', line)
        line = re.sub(r'(\*\*|__)(.*?)\1', r'\2', line)
        line = re.sub(r'(\*|_)(.*?)\1', r'\2', line)
        line = re.sub(r'~~(.*?)~~', r'\1', line)
        return line.strip()

    lines = text.split('\n')
    cleaned_lines = [clean_line(line) for line in lines]
    cleaned_text = '\n'.join(cleaned_lines)
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', cleaned_text)
    return cleaned_text.strip()

st.set_page_config(layout="wide")

st.title('ChatGPT Output Cleaner by WDSL (Structure Preserving)')

st.write('This app removes unnecessary star marks, Markdown headers, and unwanted styles from ChatGPT output while preserving the text structure.')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Input Text')
    input_text = st.text_area('', height=400, key='input_area')
    if st.button('Clean Text'):
        if input_text:
            cleaned_text = clean_text(input_text)
            st.session_state['cleaned_text'] = cleaned_text
        else:
            st.warning('Please enter some text to clean.')

with col2:
    st.subheader('Cleaned Output')
    if 'cleaned_text' in st.session_state:
        st.text_area('', value=st.session_state['cleaned_text'], height=400, key='output_area')

        

