from PySide2.QtWidgets import QMainWindow, QFileDialog
from src.ui.mainWindow_ui import Ui_MainWindow
from pytube import YouTube
from VideoPlayer import VideoPlayer


class MainWindow(QMainWindow):
    def __init__(self):
        # Init
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_preview.clicked.connect(self.preview)
        self.ui.btn_directory.clicked.connect(self.find_directory)
        
    def download(self):
        url = self.ui.le_url.text()
        output = self.ui.le_output.text()
        #yt = YouTube(url)
        YouTube(url).streams[0].download(output)
    
    def preview(self):
        url = self.ui.le_url.text()
        newWidget = VideoPlayer(url)
        self.ui.sw_player.addWidget(newWidget)
        self.ui.sw_player.setCurrentWidget(newWidget)
        '''
        player = QMediaPlayer()
        video_widget = QVideoWidget()
        player.setVideoOutput(video_widget)
        self.ui.sw_player.addWidget(video_widget)
        video_widget.setStyleSheet('background-color: rgb(25, 55, 25)')
        url = self.ui.le_url.text()
        player.setMedia(QUrl(url))
        #player.setMedia(QUrl.fromLocalFile('D:/teste.mp4'))
        video_widget.setGeometry(10,10,300,300)
        video_widget.show()
        player.play()
        print(player.state())
        '''
        
    
    def find_directory(self):
        dir = QFileDialog.getExistingDirectory(self, 
              self.tr("Open Directory"), self.tr("/home"))
        self.ui.le_output.setText(dir)
    
    def check_url_is_valid(self):
        pass # funtions donwload and preview will use it
    