import streamlit as st
from audio_chunking import split_audio_in_chunks
from stt_processing import send_audio_for_stt
from ner_service import extract_company_name_from_text
from datetime import timedelta
import os
from pydub.utils import mediainfo
import spacy

# Download the spaCy model if it's not already installed
try:
    spacy.load("en_core_web_sm")  # Try loading the model to check if it's installed
except OSError:
    spacy.cli.download("en_core_web_sm")  # Download it if it's not installed


# Function to get audio duration
def get_audio_duration(filename):
    """
    Calculate the duration of the audio file in seconds using pydub.
    """
    audio_info = mediainfo(filename)
    return float(audio_info['duration'])

# Function to process the audio and extract information
def process_audio(path):
    # Step 1: Split the audio into chunks
    st.write(f"Splitting audio file: {path}")
    split_audio_in_chunks(path)

    # Initialize start time for the first chunk
    start_time = timedelta(hours=0, minutes=0, seconds=0)

    results = []

    # List of chunks sorted by filename to maintain the correct order
    chunks = sorted(os.listdir('audio_chunks'), key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Step 2: Process each chunk with Speech-to-Text and store timestamps
    st.write("Processing chunks for Speech-to-Text...")
    for chunk in chunks:
        if chunk.endswith(".wav"):
            st.write(f"Sending {chunk} for STT...")

            # Process the chunk for STT
            transcription = send_audio_for_stt(f'audio_chunks/{chunk}')
            st.write(f"Transcription for {chunk}: {transcription}")
            
            # Step 3: Extract company names from transcription using NER
            companies = extract_company_name_from_text(transcription)
            
            # Step 4: Collect results
            if companies:
                for company in companies:
                    results.append({
                        "company": company,
                        "chunk": chunk,
                        "start_time": str(start_time),
                        "end_time": str(start_time + timedelta(seconds=get_audio_duration(f'audio_chunks/{chunk}')))
                    })
            else:
                results.append({
                    "company": "No company detected",
                    "chunk": chunk,
                    "start_time": str(start_time),
                    "end_time": str(start_time + timedelta(seconds=get_audio_duration(f'audio_chunks/{chunk}')))
                })
            
            # Step 5: Update start time for the next chunk
            start_time = start_time + timedelta(seconds=get_audio_duration(f'audio_chunks/{chunk}'))

    return results

# Streamlit UI for the application
def main():
    st.title("Commercial Detection from TV Channel Audio")
    st.write(
        """
        Upload an audio file and the system will detect the commercials, extract company names, and display the timestamp information.
        """
    )

    # Create 'uploaded_files' directory if it doesn't exist
    if not os.path.exists("uploaded_files"):
        os.makedirs("uploaded_files")

    # File uploader for audio file
    uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "mp4", "m4a"])

    if uploaded_file is not None:
        # Save uploaded file to the 'uploaded_files' directory
        file_path = os.path.join("uploaded_files", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write(f"Processing file: {uploaded_file.name}")
        
        # Process the audio and extract results
        results = process_audio(file_path)

        # Display results in a table using st.dataframe
        if results:
            st.subheader("Detected Commercials:")
            st.write("The following companies were detected in the audio, along with the timestamps:")

            # Create a dataframe for better visualization
            import pandas as pd
            df = pd.DataFrame(results)
            st.dataframe(df)  # Display the results as a table
        else:
            st.write("No commercials detected in the audio.")
    else:
        st.write("Please upload an audio file to begin processing.")

if __name__ == "__main__":
    main()
