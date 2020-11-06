# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gb_inputs = QGroupBox(self.centralwidget)
        self.gb_inputs.setObjectName(u"gb_inputs")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_inputs.sizePolicy().hasHeightForWidth())
        self.gb_inputs.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(self.gb_inputs)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_inputs)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_url = QLineEdit(self.gb_inputs)
        self.le_url.setObjectName(u"le_url")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_url)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_output = QLineEdit(self.gb_inputs)
        self.le_output.setObjectName(u"le_output")

        self.horizontalLayout_2.addWidget(self.le_output)

        self.btn_directory = QToolButton(self.gb_inputs)
        self.btn_directory.setObjectName(u"btn_directory")

        self.horizontalLayout_2.addWidget(self.btn_directory)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_preview = QPushButton(self.gb_inputs)
        self.btn_preview.setObjectName(u"btn_preview")

        self.horizontalLayout.addWidget(self.btn_preview)

        self.btn_download = QPushButton(self.gb_inputs)
        self.btn_download.setObjectName(u"btn_download")

        self.horizontalLayout.addWidget(self.btn_download)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_2 = QLabel(self.gb_inputs)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout.addWidget(self.gb_inputs)

        self.sw_player = QStackedWidget(self.centralwidget)
        self.sw_player.setObjectName(u"sw_player")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sw_player.sizePolicy().hasHeightForWidth())
        self.sw_player.setSizePolicy(sizePolicy1)
        self.sw_player.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.sw_player)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube Downloader", None))
        self.gb_inputs.setTitle(QCoreApplication.translate("MainWindow", u"Inputs", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.btn_directory.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_preview.setText(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Directory output:", None))
    # retranslateUi

