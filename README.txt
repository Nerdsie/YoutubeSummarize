Summarize any YouTube video with OpenAI Whisper/ChatGPT
Includes a Firefox addon for interfacing with the summarizer.

Requirements:
 * FFMPEG
 * Python

Cost:
  Rough estimates from running this a few times, a 20-minute video costs about $0.15 total.
  Price will vary depending on the length of the video.
  Longer videos have their transcripts split into multiple chatgpt requests to stay under token limit, so the cost will be higher.

Setup:
    1. Install requirements - `pip install -r requirements.txt`
    2. Create .env at root level with 'OPENAI_KEY=YOUR_KEY_HERE'
    3. Run `python main.py`

Limitations:
  Currently audio files can exceed the max size limit for Whisper resulting in an error/crash.