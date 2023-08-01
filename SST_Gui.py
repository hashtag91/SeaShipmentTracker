from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon
import sys

class mainWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        
class mainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shipments Tracking")
        self.resize(800,600)
        ico = QIcon("img/icon.png")
        self.setWindowIcon(ico)
        self.setCentralWidget(mainWidget())
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    win = mainWin()
    sys.exit(App.exec())