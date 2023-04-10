from flask import Flask, request

from Server.chatgpt import summarize_from_url


def create_server():
    app = Flask(__name__)

    @app.route('/summarize', methods=['GET'])
    def summarize():
        video_url = request.args.get('videoUrl')
        print('URL', video_url)
        return summarize_from_url(video_url)

    app.run()
