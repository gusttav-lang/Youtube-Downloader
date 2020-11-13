from PySide2 import QObject
from pytube import YouTube


class StreamLoader(QObject):
    def __init__(self, url : str):
        self.yt = YouTube(url)
