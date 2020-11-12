from PySide2.QtWidgets import QMainWindow, QFileDialog
from src.ui.mainWindow_ui import Ui_MainWindow
from pytube import YouTube
from VideoPlayer import VideoPlayer
from downloadList import DownloadList


class MainWindow(QMainWindow):
    def __init__(self):
        # Init
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_preview.clicked.connect(self.preview)
        self.ui.btn_directory.clicked.connect(self.find_directory)
        
        self.url = ''
        self.output = ''
        self.resolution = None
        self.audio_only = None
        self.ui.le_url.textChanged.connect(self.set_url)
        self.ui.le_url.textChanged.connect(self.set_output)
        self.ui.rb_144.toggled.connect(self.quality_filter_changed)
        self.ui.rb_240.toggled.connect(self.quality_filter_changed)
        self.ui.rb_360.toggled.connect(self.quality_filter_changed)
        self.ui.rb_480.toggled.connect(self.quality_filter_changed)
        self.ui.rb_720.toggled.connect(self.quality_filter_changed)
        self.ui.rb_1080.toggled.connect(self.quality_filter_changed)
        self.ui.rb_all.toggled.connect(self.quality_filter_changed)
        self.ui.cb_audio.stateChanged.connect(self.audio_olny_changed)
        
    def download(self):
        yt = YouTube(self.url).streams.filter(resolution=self.resolution, only_audio=self.audio_only)
        print(type(yt))
        download_dialog = DownloadList(yt)
        download_dialog.exec_()
        #YouTube(url).streams[0].download(output)
    
    def preview(self):
        newWidget = VideoPlayer(self.url)
        self.ui.sw_player.addWidget(newWidget)
        self.ui.sw_player.setCurrentWidget(newWidget)        
    
    def find_directory(self):
        dir = QFileDialog.getExistingDirectory(self, 
              self.tr("Open Directory"), self.tr("/home"))
        self.ui.le_output.setText(dir)

    def check_url_is_valid(self):
        pass # funtions donwload and preview will use it

    def set_url(self, text : str):
        self.url = text

    def set_output(self, text : str):
        self.output = text
        
    def quality_filter_changed(self):
        if (self.ui.rb_144.isChecked()):
            self.resolution = '144p'
        elif (self.ui.rb_240.isChecked()):
            self.resolution = '240p'
        elif (self.ui.rb_360.isChecked()):
            self.resolution = '360p'
        elif (self.ui.rb_480.isChecked()):
            self.resolution = '480p'
        elif (self.ui.rb_720.isChecked()):
            self.resolution = '720p'
        elif (self.ui.rb_1080.isChecked()):
            self.resolution = '1080p'
        elif (self.ui.rb_all.isChecked()):
            self.resolution = None
        print(self.resolution)
    
    def audio_olny_changed(self):
        if (self.ui.cb_audio.isChecked()):
            self.audio_only = True
        else:
            self.audio_only = None # just cancel this filter
            
        print(self.audio_only)
    