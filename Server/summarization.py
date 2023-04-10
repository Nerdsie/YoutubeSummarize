class Summarization:
    def __init__(self, url):
        self.url = url
        self.videoId = url.split("watch?v=")[1]
        self.download()
        self.transribe()
        self.summarize()
        self.clean_up()

    def download(self):
        pass

    def summarize(self):
        pass