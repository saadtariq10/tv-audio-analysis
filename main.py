# from audio_chunking import split_audio_in_chunks
# from stt_processing import send_audio_for_stt
# import os

# def process_audio(path):
#     # Step 1: Split the audio into chunks
#     print(f"Splitting audio file: {path}")
#     split_audio_in_chunks(path)

#     # Step 2: Process each chunk with Speech-to-Text
#     print("Processing chunks for Speech-to-Text...")
#     for chunk in os.listdir('audio_chunks'):
#         if chunk.endswith(".wav"):
#             print(f"Sending {chunk} for STT...")
#             text = send_audio_for_stt(f'audio_chunks/{chunk}')
#             print(f"Transcription for {chunk}: {text}")

# if __name__ == '__main__':
#     # Get the path of the audio file from user
#     path = input("Enter the audio file path (supports .mp3, .wav, .mp4, .m4a): ")
    
#     # Call the function to split the audio into chunks and process STT
#     process_audio(path)




from audio_chunking import split_audio_in_chunks
from stt_processing import send_audio_for_stt
from ner_service import extract_company_name_from_text  # Import NER service
from datetime import timedelta
import os
from pydub.utils import mediainfo

def process_audio(path):
    # Step 1: Split the audio into chunks
    print(f"Splitting audio file: {path}")
    split_audio_in_chunks(path)
    
    # Initialize start time for the first chunk
    start_time = timedelta(hours=0, minutes=0, seconds=0)

    # List of chunks sorted by filename to maintain the correct order
    chunks = sorted(os.listdir('audio_chunks'), key=lambda x: int(x.split('_')[1].split('.')[0]))

    # Step 2: Process each chunk with Speech-to-Text and store timestamps
    print("Processing chunks for Speech-to-Text...")
    for chunk in chunks:
        if chunk.endswith(".wav"):
            print(f"Sending {chunk} for STT...")

            # Process the chunk for STT
            transcription = send_audio_for_stt(f'audio_chunks/{chunk}')
            print(f"Transcription for {chunk}: {transcription}")
            
            # Step 3: Extract company names from transcription using NER
            companies = extract_company_name_from_text(transcription)
            
            # Step 4: Print the results
            if companies:
                for company in companies:
                    print(f"Company detected in {chunk}: {company}")
            else:
                print(f"No company detected in {chunk}.")
            
            # Step 5: Track timestamps for when the commercial aired
            duration = get_audio_duration(f'audio_chunks/{chunk}')
            end_time = start_time + timedelta(seconds=duration)

            print(f"Commercial aired from {str(start_time)} to {str(end_time)}")
            
            # Update start time for the next chunk
            start_time = end_time

def get_audio_duration(filename):
    """
    Calculate the duration of the audio file in seconds using pydub.
    """
    audio_info = mediainfo(filename)
    return float(audio_info['duration'])

if __name__ == '__main__':
    # Get the path of the audio file from user
    path = input("Enter the audio file path (supports .mp3, .wav, .mp4, .m4a): ")
    
    # Call the function to split the audio into chunks and process STT, NER, and timestamp
    process_audio(path)
