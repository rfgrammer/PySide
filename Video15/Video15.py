import sys

from PySide.QtGui import *

import mainGui


class MainDialog(QDialog, mainGui.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()

