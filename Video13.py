import sys

from PySide.QtCore import *
from PySide.QtGui import *

from Video14 import showGui


class MainDialog(QDialog, showGui.Ui_mainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.showButton, SIGNAL("clicked()"), self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.information(self, "Hello!", "Hello there, " + self.nameEdit.text())


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
