
from pydub import AudioSegment
import os

def split_audio_in_chunks(path="long_audio.mp3", chunk_length_ms=30000):  # Default chunk length is 5 minutes (300,000 ms)
    # Load audio from file, pydub handles different formats including mp3, wav, mp4, m4a
    audio = AudioSegment.from_file(path)

    # Create a directory to store the audio chunks
    try:
        os.mkdir('audio_chunks')
    except FileExistsError:
        pass

    # Move into the directory to store the audio files
    os.chdir('audio_chunks')
    
    # Calculate the number of chunks
    num_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

    for i in range(num_chunks):
        # Calculate the start and end time of the chunk
        start_time = i * chunk_length_ms
        end_time = min((i + 1) * chunk_length_ms, len(audio))  # Ensure the last chunk doesn't exceed audio length

        # Extract the chunk
        chunk = audio[start_time:end_time]

        # Export the chunk as a new .wav file
        filename = f"chunk_{i+1}.wav"
        print(f"Saving {filename}")
        chunk.export(filename, format="wav")

    # Move back to the original directory
    os.chdir('..')







