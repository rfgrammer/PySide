from PySide.QtGui import *
from PySide.QtCore import *
import sys


class MainDialog(QDialog):

    myOwnSignal = Signal((int,), (str,))

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)

        self.btn1 = QPushButton("Button!")

        layout = QHBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)
        self.btn1.clicked.connect(self.btn1clicked)

        self.myOwnSignal.connect(self.myOwnSignalEmitted)
        self.myOwnSignal[str].connect(self.myOwnSignalEmitted)

    def btn1clicked(self):
        # for integer parameter
        self.myOwnSignal[int].emit(10)
        # # for string parameter
        # self.myOwnSignal[str].emit("Hello World")

    def myOwnSignalEmitted(self, parm):
        print("SIGNAL EMITTED!  " + str(parm))
        print(type(parm))


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
