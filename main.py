from PySide2.QtWidgets import QApplication
import sys
from PySide2.QtGui import QIcon
import os
from PySide2.QtCore import Qt

sys.path.append("src")
sys.path.append("src/ui")

if __name__ == "__main__":
    from src.mainWindow import MainWindow
    app = QApplication(sys.argv)
    
    # setting the icon in applicantion and taskbar:
    import ctypes
    myappid = 'pythonw' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(scriptDir + os.path.sep + 'icons/logo.png'))
    
    #Remove button "?" from dialogs:
    QApplication.setAttribute(Qt.AA_DisableWindowContextHelpButton) 
    
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
