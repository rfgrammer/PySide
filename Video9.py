# Dumb dialogs : no data sharing between parent dialog and child dialog

import sys
from PySide.QtGui import *
from PySide.QtCore import *

__appname__ ="Ninth Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        btn = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)
        self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)

    def dialogOpen(self):
        dialog = Dialog()
        if dialog.exec_():
            # run in case SLOT("accept()") : OK
            self.label1.setText("SpinBox value is " + str(dialog.spinbox.value()))
            self.label2.setText("Checkbox is " + str(dialog.checkbox.isChecked()))
        else:
            # run in case SLOT("reject()") : Cancel
            QMessageBox.warning(self, __appname__, "Dialog cancelled.")


class Dialog(QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkbox = QCheckBox("Check me out!")
        self.spinbox = QSpinBox()
        buttonOk = QPushButton("OK")
        buttonCancel = QPushButton("Cancel")

        layout = QGridLayout()
        layout.addWidget(self.spinbox, 0, 0)
        layout.addWidget(self.checkbox, 0, 1)
        layout.addWidget(buttonCancel)
        layout.addWidget(buttonOk)
        self.setLayout(layout)

        self.connect(buttonOk, SIGNAL("clicked()"), SLOT("accept()"))
        self.connect(buttonCancel, SIGNAL("clicked()"), SLOT("reject()"))


def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
