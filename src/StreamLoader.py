from PySide2.QtCore import QObject, Signal
from pytube import YouTube


class StreamLoader(QObject):
    total_bytes = Signal(int)
    bytes_remaining = Signal(int)
    finished = Signal()
    
    def __init__(self, url : str):
        super().__init__()
        self.yt = YouTube(url)
        self.resolution = None
        self.audio_only = None
        self.item_for_download = 0
        self.output = ''
        self.is_first = True
        self.file_size = 0
        
    def set_resolution(self, resolution):
        self.resolution = resolution
        
    def set_audio_only(self, audio_only):
        self.audio_only = audio_only
    
    def set_item_for_download(self, item_for_download):
        self.item_for_download = item_for_download
        
    def set_output(self, output):
        self.output = output
    
    def start_thread(self):
        self.yt.streams.filter(resolution=self.resolution, only_audio=self.audio_only)[self.item_for_download].download(self.output)
        
    def show_progress_bar(self, stream, chunk, bytes_remaining):
        if (self.is_first):
            self.total_bytes.emit(bytes_remaining)
            self.file_size = bytes_remaining
            self.is_first = False
        self.bytes_remaining.emit(self.file_size - bytes_remaining)
        if (bytes_remaining == 0):
            self.finished.emit()
    