# Introducing QMainWindows class

from PySide.QtGui import *
from PySide.QtCore import *
import sys

import mainGui


class MainWindow(QMainWindow, mainGui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.actionExit.triggered.connect(self.exit_application)
        # self.connect(self.actionExit, SIGNAL("triggered()"), self.exit_application)

    def exit_application(self):
        sys.exit(0)


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()


