# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'downloadList.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_downloadList(object):
    def setupUi(self, downloadList):
        if not downloadList.objectName():
            downloadList.setObjectName(u"downloadList")
        downloadList.resize(1237, 300)
        self.gridLayout = QGridLayout(downloadList)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(downloadList)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.btn_download = QPushButton(downloadList)
        self.btn_download.setObjectName(u"btn_download")

        self.gridLayout.addWidget(self.btn_download, 1, 0, 1, 1)


        self.retranslateUi(downloadList)

        QMetaObject.connectSlotsByName(downloadList)
    # setupUi

    def retranslateUi(self, downloadList):
        downloadList.setWindowTitle(QCoreApplication.translate("downloadList", u"Choose file", None))
        self.btn_download.setText(QCoreApplication.translate("downloadList", u"Download", None))
    # retranslateUi

