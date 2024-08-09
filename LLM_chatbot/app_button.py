from dotenv import load_dotenv
import os
import google.generativeai as genai
import pandas as pd
from contextlib import redirect_stdout
from io import StringIO
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Load Google API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")

def get_gemini(Question):
    # Assuming model.generate_content is a function that generates a response based on the input question
    response = model.generate_content(Question)
    return f"{response.text}"

# Streamlit App
st.title("Gemini Pro Generator")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM sensor_data;', ttl="10m")

# User Input
variable = st.text_input("Enter the prompt:")

# Define a function to generate the code and execute it
def generate_and_execute_code(variable):
    question = f"Use the dataframe df containing sensor data from the glider from 'conn = st.connection('postgresql', type='sql') and df = conn.query('SELECT * FROM sensor_data;', ttl='10m')  with columns list({df.columns}) with time in this datetime format 2022-01-01 01:00:00 and generate just only the python code and display using st.plotly_chart(fig) with st.header taskname and st.write for description for the task: {variable} (only the code without showing output)"
    response = get_gemini(question)
    slice1 = response.replace('python', "")
    exec_code = slice1.split("```")[1]
    #exec_code = formatted_string.split('Output:')[0]
    return exec_code

# Store state
if 'exec_code' not in st.session_state:
    st.session_state.exec_code = ""

if variable:
    # Generate response using Gemini Pro
    st.session_state.exec_code = generate_and_execute_code(variable)

# Regenerate button
if st.button('Regenerate'):
    if variable:
        st.session_state.exec_code = generate_and_execute_code(variable)

print(st.session_state.exec_code)
st.subheader("Captured Output:")
try:
    with StringIO() as output_buffer:
        with redirect_stdout(output_buffer):
            exec(st.session_state.exec_code)
except Exception as e:
    st.write(f"An error occurred: {e}")



#Hiding the useless
hide_menu_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)