from PyQt4 import QtGui
from PyQt4.QtGui import QColor, QPaintEvent

m_nInitialX = 0.0
m_nInitialY = 0.0


# my line abstraction
class MyLine:
    x1, y1, x2, y2 = .0, .0, .0, .0
    width = .0
    px, py = (.0, .0)
    draw_point = False

    def __init__(self, x1, y1, x2, y2, width):
        self.x1, self.y1, self.x2, self.y2 = (x1, y1, x2, y2)
        self.width = width

    def is_in_line(self, x, y):
        # mark a position in the line
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        print(m*(x-self.x1)-(y-self.y1))
        if abs((m*(x-self.x1) - (y-self.y1))) <= self.width/2:
            self.draw_point = True
            return True
        else:
            return False

    def add_red_point(self, x, y):
        self.px, self.py = (x, y)

    def draw(self, widget):
        painter = QtGui.QPainter(widget)
        pen = QtGui.QPen()
        pen.setWidth(self.width)
        painter.setPen(pen)
        painter.drawLine(self.x1, self.y1, self.y2, self.y2)

        if self.draw_point:
            pen.setColor(QColor(255, 0, 0))
            painter.setPen(pen)
            painter.drawPoint(self.px, self.py)
        painter.end()


line = MyLine(10, 10, 90, 90, width=10)  # <-- my line abstraction


class LineLabel(QtGui.QLabel):

    def __init__(self, parent=None):
        super(LineLabel, self).__init__(parent)
        self.setMinimumSize(100, 100)
        self.setMaximumSize(100, 100)

    # always redraw when needed
    def paintEvent(self, e):
        print("draw!")
        line.draw(self)

    def mousePressEvent(self, event):
        # mark clicked position in line
        m_nInitialX = event.pos().x()
        m_nInitialY = event.pos().y()
        if line.is_in_line(m_nInitialX, m_nInitialY):
            line.add_red_point(m_nInitialX, m_nInitialY)
            self.repaint()


def test():
    form = QtGui.QWidget()
    label = LineLabel(form)
    form.show()
    return form

import sys

app = QtGui.QApplication(sys.argv)
window = test()
sys.exit(app.exec_())
