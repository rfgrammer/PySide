# Built-in dialog

import sys
from PySide.QtGui import *
from PySide.QtCore import *


__appname__ = "Eight Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close...")

        self.connect(openButton, SIGNAL("clicked()"), self.open)
        self.connect(saveButton, SIGNAL("clicked()"), self.save)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.setWindowTitle(__appname__)

    def open(self):
        defaultDir = "."
        fileobj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=defaultDir, filter="Text files (*.txt)")

        print(fileobj)
        print(type(fileobj))

        fileName = fileobj[0]

        file = open(fileName, "r")
        read = file.read()
        file.close()
        print read

    def save(self):
        defaultDir = "."

        fileobj = QFileDialog.getSaveFileName(self, __appname__, dir=defaultDir, filter="Text Files (*.txt)")

        print(fileobj)
        print(type(fileobj))

        contents = "Hello World"

        fileName = fileobj[0]

        open(fileName, "w").write(contents)


def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()

