from PySide2.QtWidgets import QDialog, QListWidgetItem
from src.ui.downloadList_ui import Ui_downloadList

class DownloadList(QDialog):
    '''
    Dialog used to show the download options. User selects the wanted option
    '''
    def __init__(self, videos_list):
        super().__init__()
        self.ui = Ui_downloadList()
        self.ui.setupUi(self)
        for i in range(len(videos_list)):
            list_item = QListWidgetItem()
            list_item.setText(str(videos_list[i]))
            self.ui.listWidget.addItem(list_item)
        
        self.ui.listWidget.setCurrentRow(0)
        self.ui.btn_download.clicked.connect(self.download)
        self.currentItem = 0
        self.download_pressed = False
        
    def download(self):
        self.currentItem = self.ui.listWidget.currentRow()
        self.download_pressed = True
        self.close()