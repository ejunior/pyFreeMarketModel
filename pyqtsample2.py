from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys


class Main(QWidget):
    def __init__(self, parent):
        super(Main, self).__init__(parent)

        self.resize(300, 300)
        vBox = QVBoxLayout(self)
        view = View(self)
        vBox.addWidget(view)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            sys.exit()


class View(QGraphicsView):
    def __init__(self, parent):
        super(View, self).__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setSceneRect(QRectF(self.viewport().rect()))

    def mousePressEvent(self, event):
        self.start = event.pos()

    def mouseReleaseEvent(self, event):
        self.stop = event.pos()
        line = Line(self, self.start, self.stop)
        self.scene.addItem(line)


class Line(QGraphicsLineItem):
    def __init__(self, parent, *args):
        # args = start, stop
        points = map(parent.mapToScene, args)
        (start, stop) = map(QPointF, points)

        # self.line = QLineF(start, stop)
        super(Line, self).__init__(self.line)


def run():
    app = QApplication(sys.argv)
    a = Main(None)
    a.show()
    sys.exit(app.exec_())


run()
