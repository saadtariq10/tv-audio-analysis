
# from pydub import AudioSegment
# import os

# def split_audio_in_chunks(path="long_audio.mp3", chunk_length_ms=30000):  # Default chunk length is 5 minutes (300,000 ms)
#     # Load audio from file, pydub handles different formats including mp3, wav, mp4, m4a
#     audio = AudioSegment.from_file(path)

#     # Create a directory to store the audio chunks
#     try:
#         os.mkdir('audio_chunks')
#     except FileExistsError:
#         pass

#     # Move into the directory to store the audio files
#     os.chdir('audio_chunks')
    
#     # Calculate the number of chunks
#     num_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

#     for i in range(num_chunks):
#         # Calculate the start and end time of the chunk
#         start_time = i * chunk_length_ms
#         end_time = min((i + 1) * chunk_length_ms, len(audio))  # Ensure the last chunk doesn't exceed audio length

#         # Extract the chunk
#         chunk = audio[start_time:end_time]

#         # Export the chunk as a new .wav file
#         filename = f"chunk_{i+1}.wav"
#         print(f"Saving {filename}")
#         chunk.export(filename, format="wav")

#     # Move back to the original directory
#     os.chdir('..')







# from pydub import AudioSegment
# import os

# def split_audio_in_chunks(path="long_audio.mp3", chunk_length_ms=30000):  # Default chunk length is 5 minutes (300,000 ms)
#     # Load audio from file, pydub handles different formats including mp3, wav, mp4, m4a
#     audio = AudioSegment.from_file(path)

#     # Create a directory to store the audio chunks
#     try:
#         os.mkdir('audio_chunks')
#     except FileExistsError:
#         pass

#     # Move into the directory to store the audio files
#     os.chdir('audio_chunks')
    
#     # Calculate the number of chunks
#     num_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

#     for i in range(num_chunks):
#         # Calculate the start and end time of the chunk
#         start_time = i * chunk_length_ms
#         end_time = min((i + 1) * chunk_length_ms, len(audio))  # Ensure the last chunk doesn't exceed audio length

#         # Extract the chunk
#         chunk = audio[start_time:end_time]

#         # Export the chunk as a new .wav file
#         filename = f"chunk_{i+1}.wav"
#         print(f"Saving {filename}")
#         chunk.export(filename, format="wav")

#     # Move back to the original directory
#     os.chdir('..')








# from pydub import AudioSegment
# import os

# def split_audio_in_chunks(path="long_audio.mp3", chunk_length_ms=30000):  # Default chunk length is 30 seconds (30,000 ms)
#     # Load audio from file, pydub handles different formats including mp3, wav, mp4, m4a
#     audio = AudioSegment.from_file(path)

#     # Create a directory to store the audio chunks
#     temp_folder = 'audio_chunks'
#     if not os.path.exists(temp_folder):
#         os.mkdir(temp_folder)
#     else:
#         # Cleanup the folder before storing new chunks
#         for file in os.listdir(temp_folder):
#             file_path = os.path.join(temp_folder, file)
#             if os.path.isfile(file_path):
#                 os.remove(file_path)

#     # Move into the directory to store the audio files
#     os.chdir(temp_folder)

#     # Calculate the number of chunks
#     num_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

#     for i in range(num_chunks):
#         # Calculate the start and end time of the chunk
#         start_time = i * chunk_length_ms
#         end_time = min((i + 1) * chunk_length_ms, len(audio))  # Ensure the last chunk doesn't exceed audio length

#         # Extract the chunk
#         chunk = audio[start_time:end_time]

#         # Export the chunk as a new .wav file
#         filename = f"chunk_{i+1}.wav"
#         print(f"Saving {filename}")
#         chunk.export(filename, format="wav")

#     # Move back to the original directory
#     os.chdir('..')

#     # Optionally, delete the folder after use
#     for file in os.listdir(temp_folder):
#         file_path = os.path.join(temp_folder, file)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#     os.rmdir(temp_folder)

# # Test the function with an example file
# split_audio_in_chunks("long_audio.mp3")











from pydub import AudioSegment
import os

def split_audio_in_chunks(path, chunk_length_ms=30000):
    """
    Split the audio file at the given 'path' into chunks of 'chunk_length_ms' milliseconds.
    """
    # Load audio from file, pydub handles different formats including mp3, wav, mp4, m4a
    audio = AudioSegment.from_file(path)

    # Create a temporary folder to store the audio chunks
    temp_folder = 'audio_chunks'
    if not os.path.exists(temp_folder):
        os.mkdir(temp_folder)
    else:
        # Clean up the folder before storing new chunks
        for file in os.listdir(temp_folder):
            file_path = os.path.join(temp_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # Calculate the number of chunks
    num_chunks = len(audio) // chunk_length_ms + (1 if len(audio) % chunk_length_ms != 0 else 0)

    # List to store the filenames of the chunks
    chunk_files = []

    for i in range(num_chunks):
        # Calculate the start and end time of the chunk
        start_time = i * chunk_length_ms
        end_time = min((i + 1) * chunk_length_ms, len(audio))  # Ensure the last chunk doesn't exceed audio length

        # Extract the chunk
        chunk = audio[start_time:end_time]

        # Export the chunk as a new .wav file
        filename = f"chunk_{i+1}.wav"
        chunk.export(os.path.join(temp_folder, filename), format="wav")
        chunk_files.append(os.path.join(temp_folder, filename))

    return chunk_files
