from PySide2.QtWidgets import QMainWindow, QFileDialog, QProgressDialog
from src.ui.mainWindow_ui import Ui_MainWindow
from VideoPlayer import VideoPlayer
from downloadList import DownloadList
from PySide2.QtCore import QThread
from StreamLoader import StreamLoader


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
        self.ui.le_output.textChanged.connect(self.set_output)
        self.ui.rb_144.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_240.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_360.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_480.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_720.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_1080.toggled.connect(self.resolution_filter_changed)
        self.ui.rb_all.toggled.connect(self.resolution_filter_changed)
        self.ui.cb_audio.stateChanged.connect(self.audio_olny_changed)
        
        self.download_thread = QThread()        
        self.progress_dialog = QProgressDialog()   
        self.progress_dialog.hide()
        
    def download(self):        
        yt = StreamLoader(self.url)
        download_dialog = DownloadList(yt.yt.streams.filter(resolution=self.resolution, only_audio=self.audio_only))
        download_dialog.exec_()
        
        item_for_download = download_dialog.currentItem
        yt.yt.register_on_progress_callback(yt.show_progress_bar)    
        
        #temp:        
        yt.total_bytes.connect(self.print_bytes)
        yt.bytes_remaining.connect(self.print_bytes)
        
        
        yt.set_resolution(self.resolution)
        yt.set_audio_only(self.audio_only)
        yt.set_output(self.output)
        yt.set_item_for_download(item_for_download)
        
        
        yt.moveToThread(self.download_thread)
        self.download_thread.started.connect(yt.start_thread)         
        self.progress_dialog.setLabelText('Downloading')
        yt.total_bytes.connect(self.progress_dialog.setMaximum)
        yt.bytes_remaining.connect(self.progress_dialog.setValue)
        self.progress_dialog.show()
        
        self.download_thread.start()
        
    def preview(self):
        newWidget = VideoPlayer(self.url)
        self.ui.sw_player.addWidget(newWidget)
        self.ui.sw_player.setCurrentWidget(newWidget)        
    
    def find_directory(self):
        dir = QFileDialog.getExistingDirectory(self, 
              self.tr("Open Directory"), self.tr("/home"))
        self.ui.le_output.setText(dir)

    def check_url_is_valid(self):
        pass # functions donwload and preview will use it

    def set_url(self, text : str):
        self.url = text

    def set_output(self, text : str):
        self.output = text
        
    def resolution_filter_changed(self):
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
    
    def audio_olny_changed(self):
        if (self.ui.cb_audio.isChecked()):
            self.audio_only = True
        else:
            self.audio_only = None # just cancel this filter          
   
    '''def show_progress_bar(stream, chunk, file_handler, bytes_remaining):
        if (is_first[0]):
            progress_dialog[0] = QProgressDialog()
            progress_dialog[0].setLabelText('Downloading')
            total_bytes[0] = bytes_remaining
            progress_dialog[0].setRange(0, bytes_remaining)
            progress_dialog[0].show()
            is_first[0] = False
            print(is_first[0])
        progress_dialog[0].setValue(total_bytes[0] - bytes_remaining)'''
        
    def print_bytes(self, inteiro):
        print(inteiro)
        
    