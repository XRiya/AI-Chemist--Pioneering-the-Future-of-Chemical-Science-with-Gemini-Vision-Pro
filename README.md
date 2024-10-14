# AI Chemist: Pioneering the Future of Chemical Science with Gemini Vision Pro

AI Chemist is an innovative application designed to assist chemists in research by leveraging the power of artificial intelligence. This project utilizes the Gemini model (version 1.5 Flash) to analyze chemical inputs, identify tablets from images, and generate detailed experimental recommendations. The app aims to enhance research efficiency and foster innovation in the field of chemistry through intelligent, data-driven guidance.

## Features
- Tablet Identification: Upload an image of tablets, and the AI Chemist app will identify the tablets and provide detailed information on each.
- Experiment Design: Receive tailored experiment designs based on the input chemical structures and research objectives.
- Real-time Monitoring: Adjust and optimize reaction conditions on the fly with real-time feedback.
- Data-Driven Insights: Gain insights into chemical synthesis routes, yield, purity, and more.

## Technologies Used
- Streamlit: For building the interactive web application.
- Google Generative AI (Gemini 1.5 Flash): To analyze input data and generate content.
- Python-dotenv: To manage environment variables securely.
- Pillow: For image processing.
- PyPDF2: For handling PDF documents.
- streamlit-extras: Additional utilities to enhance the Streamlit app.

## Project Structure
- app.py: The main application file containing both the model and UI code.
- requirements.txt: List of required libraries to set up the environment.
- images/: Directory to store images used in the user interface.
- .env: Securely stores environment variables like the Google API key.
