import openai


def transcribe(videoId):
    audio_file_name = 'tmp/' + videoId + '.mp3'
    transcript_file_name = 'Server/transcriptions/' + videoId + '.txt'
    audio_file = open(audio_file_name, "rb")
    print("Transcribing audio...")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # save transcript to .txt
    print("Transcription finished!")
    with open(transcript_file_name, 'w') as f:
        f.write(str(transcript))
    return transcript


def split_transcript(transcript):
    # split transcript approximately in half. Split at the end of a sentence
    split_index = transcript.rfind(".", 0, len(transcript) // 2)
    transcript1 = transcript[:split_index] + "."
    transcript2 = transcript[split_index + 1:]
    return transcript1, transcript2
