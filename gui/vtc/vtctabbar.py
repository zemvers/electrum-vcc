from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VtcTabBar(QTabBar):
    def __init__(self, parent=None):
        super(VtcTabBar, self).__init__(parent)

    def tabSizeHint(self, index):
        return QSize(150, 150)

    def paintEvent(self, event):
        #todo:
        pass
