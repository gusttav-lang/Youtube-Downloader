from PySide2.QtWidgets import QDialog, QListWidgetItem
from src.ui.downloadList_ui import Ui_downloadList

class DownloadList(QDialog):
    def __init__(self, videos_list):
        super().__init__()
        self.ui = Ui_downloadList()
        self.ui.setupUi(self)
        for i in range(len(videos_list)):
            list_item = QListWidgetItem()
            list_item.setText(str(videos_list[i]))
            self.ui.listWidget.addItem(list_item)