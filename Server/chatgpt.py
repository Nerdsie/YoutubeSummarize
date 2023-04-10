import openai

from Server.download import download
from Server.transcribe import split_transcript, transcribe


# Summarize using the text-complete API
def text_complete(text):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt='Please summarize the following video transcript:\n' + text,
        max_tokens=200,
    )
    return response.choices[0].text


# Summarize using the chatgpt api
def chat_complete(text):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': 'Please summarize the following video transcript:'},
            {'role': 'user', 'content': text},
        ],
        max_tokens=200,
    )
    return response.choices[0].message.content


# Summarize a full text, splitting it in half if necessary (ie: if the text is too long)
def summarize_text(text):
    print("Summarizing text...")
    try:
        return chat_complete(text)
    except Exception as e:
        # TODO: Ensure exception is due to text being too long

        print(e)
        print("Error, trying to split text")
        [t1, t2] = split_transcript(text)
        sum1 = summarize_text(t1)
        sum2 = summarize_text(sum1 + t2)
        return sum2


def summarize_from_file(videoId):
    transcript = ""
    transcript_file_name = 'Server/transcriptions/' + videoId + '.txt'
    summary_file_name = 'Server/summaries/' + videoId + '.txt'
    with open(transcript_file_name, 'r') as f:
        transcript = f.read()
    summary = summarize_text(transcript)
    print("Summarization finished:")
    print(summary)
    with open(summary_file_name, 'w') as f:
        f.write(summary)
    return summary


def summarize_from_url(url):
    download(url)
    videoId = url.split("watch?v=")[1]
    transcript = transcribe(videoId)
    return summarize_from_file(videoId)
