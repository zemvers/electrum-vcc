from PyQt4.QtCore import *
from PyQt4.QtGui import *


class VtcTabBar(QTabBar):
    def __init__(self, parent=None):
        super(VtcTabBar, self).__init__(parent)
        self.tabSize = QSize(120, 120)

        self.borderColor = QColor(165, 162, 170)
        self.backgroundColor = QColor(30, 24, 43)
        self.textColor = self.borderColor
        self.highlightTextColor = QColor(255, 255, 255)
        self.highlightColor = QColor(27, 92, 46)

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
        painter.setPen(self.borderColor)
        painter.setBrush(QBrush(self.backgroundColor))
        painter.drawRect(rect)

        if is_selected:
            painter.fillRect(rect.x() + 1, rect.y() + 1, 0.05 * rect.width(),
                             rect.height(), self.highlightColor)
            self.drawText(painter, rect, self.highlightTextColor, text)
        else:
            self.drawText(painter, rect, self.textColor, text)

        iconRect = QRect(rect.x() + 0.25 * rect.width(),
                         rect.y() + 0.25 * rect.height(),
                         0.5 * rect.width(),
                         0.5 * rect.height())
        icon.paint(painter, iconRect)

    def drawText(self, painter, rect, color, text):
        painter.setPen(color)
        textRect = QRect(rect.x(), rect.y() + 0.75 * rect.height(),
                         rect.width(), 0.25 * rect.height())
        painter.drawText(textRect, Qt.AlignCenter, text)
