from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VtcTabBar(QTabBar):
    def __init__(self, parent=None):
        super(VtcTabBar, self).__init__(parent)
        self.tabSize = QSize(120, 120)

    def tabSizeHint(self, index):
        return self.tabSize

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)

        for index in range(self.count()):
            rect = self.tabRect(index)
            icon = self.tabIcon(index)
            text = self.tabText(index)
            is_selected = (self.currentIndex() == index)
            self.drawTab(painter, rect, icon, text, is_selected)

        painter.end()

    def drawTab(self, painter, rect, icon, text, is_selected):
        painter.setPen(QColor(165, 162, 170))
        painter.setBrush(QBrush(QColor(30, 24, 43)))
        painter.drawRect(rect)

        icon_y_padding = 20
        iconRect = QRect(rect.x(), rect.y() + icon_y_padding, rect.width(),
                         0.75 * rect.height() - icon_y_padding)
        icon.paint(painter, iconRect)

        textRect = QRect(rect.x(), rect.y() + 0.75 * rect.height(),
                         rect.width(), 0.25 * rect.height())
        painter.drawText(textRect, Qt.AlignCenter, text)
