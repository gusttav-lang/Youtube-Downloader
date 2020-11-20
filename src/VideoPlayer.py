from PySide2 import QtWidgets
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtCore import QUrl, Qt
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QCursor

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, url: str):        
        super(VideoPlayer, self).__init__()
        self.player = QMediaPlayer()    

        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        self.playlist = QMediaPlaylist(self.player)
        self.playlist.addMedia(QUrl(url))

        self.video_widget = QVideoWidget()
        self.player.setVideoOutput(self.video_widget)

        self.playlist.setCurrentIndex(0)
        self.player.setPlaylist(self.playlist)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.video_widget)
        self.setLayout(self.layout)

        self.player.play()
        QApplication.restoreOverrideCursor() 
        
    def mousePressEvent(self, event):
        if self.player.state() == QMediaPlayer.PausedState:
            self.player. play()
        else:
            self.player.pause()
        