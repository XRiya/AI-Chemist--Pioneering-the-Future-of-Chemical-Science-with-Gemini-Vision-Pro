# AI Chemist App
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini 1.5 Flash API and get response
def get_gemini_response(input_text, image, prompt):
    # Use the updated model name
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to prepare the image data for the model
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Define the input prompt
input_prompt = """
You are an expert pharmaceutical chemist. Your task is to analyze the image provided, identify the tablets shown, and provide detailed information about each one. Follow the steps below:

1. Examine the image carefully and identify all tablets depicted.
2. Describe the uses and functionalities of each tablet shown in the image.
3. Provide information on the intended purposes, features, and typical applications of the tablets.
4. If possible, include any notable specifications or distinguishing characteristics of each tablet.
5. Ensure clarity and conciseness in your descriptions, focusing on key details and distinguishing factors.
"""

# Initialize the Streamlit app
st.set_page_config(page_title="AI Chemist App")

st.header("AI Chemist App")

# Text input for additional instructions
input_text = st.text_input("Input Prompt: ", key="input")

# File uploader for the image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to trigger the analysis
submit = st.button("Tell me")

# If the submit button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_text, image_data, input_prompt)
    st.subheader("The Response is")
    st.write(response)
