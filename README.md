# Audio Processing with STT and NER

This project demonstrates an end-to-end pipeline for processing audio files, extracting transcriptions using Speech-to-Text (STT), and performing Named Entity Recognition (NER) to extract company names from the transcriptions. The project also splits large audio files into smaller chunks, processes each chunk for transcription, and tracks timestamps of audio segments.

## Features

- **Audio Chunking**: Split large audio files into smaller chunks to ensure manageable sizes for processing.
- **Speech-to-Text (STT)**: Convert each audio chunk into text using Groq's API and the Whisper model.
- **Named Entity Recognition (NER)**: Extract company names from the transcriptions using spaCy's pre-trained NER model.
- **Timestamp Tracking**: Track and display the start and end times for each chunk, useful for identifying when a commercial aired.
- **Temporary File Handling**: Clean up temporary audio chunks after processing to optimize space usage.

## Installation

### Prerequisites
1. Python 3.x
2. Install dependencies:

```bash
pip install pydub spacy groq
python -m spacy download en_core_web_sm
```

### Setup for Groq API Key

To use the Groq API for Speech-to-Text (STT), you'll need to add your API key to Streamlit's secrets. Add the following to your Streamlit secrets configuration:

```bash
[secrets]
GROQ_API_KEY = "your-api-key-here"
```

## Usage

### Step 1: Split the audio into chunks
The `split_audio_in_chunks` function will split the given audio file into smaller chunks, making it easier to process in segments.

### Step 2: Transcribe Audio using STT
The `send_audio_for_stt` function sends each audio chunk to Groq's API for transcription using the Whisper model.

### Step 3: Extract Company Names with NER
Using spaCy's pre-trained NER model (`en_core_web_sm`), the script identifies and extracts company names (labeled as "ORG" entities) from the transcriptions.

### Step 4: Process Audio
Run the `process_audio` function to automatically split, transcribe, and extract company names for each chunk. It will also print timestamps of when each segment aired.

```python
if __name__ == '__main__':
    # Get the path of the audio file from the user
    path = input("Enter the audio file path (supports .mp3, .wav, .mp4, .m4a): ")
    
    # Call the function to process the audio
    process_audio(path)
```

### Output
For each chunk, the script will print:
- The transcription.
- The detected company names (if any).
- The time duration of each audio segment.
- The start and end times of the commercial (or audio segment).

### Example Output

```
Splitting audio file: example.mp3
Processing chunks for Speech-to-Text...
Sending chunk_1.wav for STT...
Transcription for chunk_1: "Welcome to XYZ Corporation, your trusted partner..."
Company detected in chunk_1: XYZ Corporation
Commercial aired from 00:00:00 to 00:00:30
```

## Cleanup
After processing, the script deletes all the audio chunk files to free up space. The `clean_temp_folder` function ensures that the folder is empty after all processing is done.

## Project Structure

```
audio_processing_project/
│
├── audio_chunking.py              # Contains the function to split audio into chunks
├── stt_processing.py              # Contains the function to send audio to STT API
├── ner_service.py                 # Contains the function for NER (company name extraction)
├── models/                        # Folder containing the spaCy model
│   └── en_core_web_sm/            # Pre-trained spaCy model for NER
├── app.py                         # Main script for processing audio
├── audio_chunks/                  # Temporary folder for storing audio chunks
└── requirements.txt               # List of required packages
```

## Contributing

Feel free to fork this repository, contribute, and submit pull requests. 

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
