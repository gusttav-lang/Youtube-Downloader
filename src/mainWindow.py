from PySide2.QtWidgets import QMainWindow, QFileDialog, QProgressDialog, QMessageBox
from src.ui.mainWindow_ui import Ui_MainWindow
from VideoPlayer import VideoPlayer
from downloadList import DownloadList
from PySide2.QtCore import QThread, QUrl
from StreamLoader import StreamLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.url = ''
        self.output = ''
        self.resolution = None
        self.audio_only = None
        
        self.fill_connects()
        
        #must create here, otherwise thread is destroyed too soon:
        self.download_thread = QThread()
        self.progress_dialog = None
        self.yt = None
        
    def download(self):    
        '''
        Download the youtube URL to the output directory.
        '''
        if (self.check_url_is_valid(self.url) == False or
            self.check_url_is_valid(self.output) == False):
            self.show_error_dialog('Invalid input')
            return
        
        try:
            self.yt = StreamLoader(self.url)
        except:
            self.show_error_dialog('Invalid URL')

        download_list = self.yt.yt.streams.filter(resolution=self.resolution, only_audio=self.audio_only)
        if (len(download_list) == 0):
            self.show_error_dialog('There is not any valid file with the '
                                   'selected filter. Please updated it!')
            return
        download_dialog = DownloadList(download_list)
        download_dialog.exec_()        
        item_for_download = download_dialog.currentItem   
        if (download_dialog.download_pressed == False):
            return
        
        self.yt.set_resolution(self.resolution)
        self.yt.set_audio_only(self.audio_only)
        self.yt.set_output(self.output)
        self.yt.set_item_for_download(item_for_download)        
        
        self.progress_dialog = QProgressDialog() 
        self.progress_dialog.setWindowTitle('Downloading')
        self.progress_dialog.setCancelButton(None)
        self.yt.moveToThread(self.download_thread)
        self.download_thread.started.connect(self.yt.start_thread)  
        self.yt.finished.connect(self.download_thread.quit)
        self.yt.yt.register_on_progress_callback(self.yt.show_progress_bar)
        self.yt.total_bytes.connect(self.progress_dialog.setMaximum)
        self.yt.bytes_remaining.connect(self.progress_dialog.setValue)
        self.progress_dialog.show()
        
        self.download_thread.start()
        
    def preview(self):
        newWidget = VideoPlayer(self.url)
        self.ui.sw_player.addWidget(newWidget)
        self.ui.sw_player.setCurrentWidget(newWidget)        
    
    def find_directory(self):
        '''
        Open a QFileDialog to search the output directory
        '''
        dir = QFileDialog.getExistingDirectory(self, 
              self.tr("Open Directory"), self.tr("/home"))
        self.ui.le_output.setText(dir)

    def check_url_is_valid(self, url_to_validate : str):
        '''Validate an URL. Can be either output directory or web address'''        
        if QUrl(self.url).isValid():
            return True
        else:
            return False

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
            
    def fill_connects(self):
        '''
        Makes the connects for the necessaries signals/slots
        '''
        self.ui.btn_download.clicked.connect(self.download)
        self.ui.btn_preview.clicked.connect(self.preview)
        self.ui.btn_directory.clicked.connect(self.find_directory)
        
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
   
    def show_error_dialog(self, text : str):
        '''
        Show a error QMessageBox with text = text
        '''
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setText(text)
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.exec()
    