from qtpy.QtGui import * 
from qtpy.QtWidgets import *
from qtpy.QtCore import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.setWindowTitle("Hello World")
        label = QLabel("Hello World")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec_()