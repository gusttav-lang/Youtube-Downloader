from PySide2.QtWidgets import QApplication
import sys


sys.path.append("src")
sys.path.append("src/ui")

if __name__ == "__main__":
    from src.mainWindow import MainWindow
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
