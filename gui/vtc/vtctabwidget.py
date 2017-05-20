import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import vtctabbar


class VtcTabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(VtcTabWidget, self).__init__(parent)
        tabBar = vtctabbar.VtcTabBar(self)
        self.setTabBar(tabBar)
        self.setTabPosition(QTabWidget.West)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 840, 400)
    #window.setStyleSheet("QMainWindow { background-color: darkblue; }")
    tabWidget = VtcTabWidget(window)
    tabWidget.addTab(QLabel("Test"), "Tes&t")
    tabWidget.addTab(QLabel("Test 2"), "Test &2")
    window.setCentralWidget(tabWidget)
    window.show()
    app.exec_()
