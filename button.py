from qtpy.QtGui import * 
from qtpy.QtCore import *

import sys
from qtpy.QtCore import QObject
from qtpy import QtCore
from qtpy.QtCore import *
from qtpy.QtWidgets import *
from qtpy.QtGui import * 

class OwnEvent(QObject):
    closeMeEvent = QtCore.Signal()

class Fenster(QWidget):
    def __init__(self):
        super(Fenster, self).__init__()
        self.initMe()

    def initMe(self):
        self.sig = OwnEvent()
        self.sig.closeMeEvent.connect(self.close)
        QToolTip.setFont(QFont('SansSerif', 10))
        button = QPushButton('Drück mich', self)
        button.move(50, 50)
        button.setToolTip('wtf')  # Corrected line
        button.clicked.connect(self.push)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Button')
        self.setWindowIcon(QIcon("email.png"))
        self.show()

    def push(self):
        sender = self.sender()
        sender.move(100, 100)
        print(sender.text() + ' lol !')

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_W:
            self.sig.closeMeEvent.emit()
            

app = QApplication([])
w = Fenster()
sys.exit(app.exec_())