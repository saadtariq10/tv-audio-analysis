# #for running locally streamlit

# import os
# from groq import Groq
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Fetch the API key from the environment variables
# API_KEY = os.getenv("GROQ_API_KEY")

# # Initialize the Groq client with the API key
# client = Groq(api_key=API_KEY)

# def send_audio_for_stt(filename):
#     # Open the audio file
#     with open(filename, "rb") as file:
#         # Create a translation of the audio file
#         translation = client.audio.translations.create(
#             file=(filename, file.read()),  # Required audio file
#             model="whisper-large-v3",  # Model to use for translation
#             prompt="Specify context or spelling",  # Optional
#             response_format="json",  # Optional
#             temperature=0.0  # Optional
#         )
#         return translation.text






#for streamlit cloud
from groq import Groq
import streamlit as st

# Fetch the API key from Streamlit's secrets
API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize the Groq client with the API key
client = Groq(api_key=API_KEY)

def send_audio_for_stt(filename):
    # Open the audio file
    with open(filename, "rb") as file:
        # Create a translation of the audio file
        translation = client.audio.translations.create(
            file=(filename, file.read()),  # Required audio file
            model="whisper-large-v3",  # Model to use for translation
            prompt="Specify context or spelling",  # Optional
            response_format="json",  # Optional
            temperature=0.0  # Optional
        )
        return translation.text
