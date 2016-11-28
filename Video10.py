# Standard dialogs :
# 1. share data between parent dialog and child dialog
# 2. validate input

import sys
from PySide.QtGui import *
from PySide.QtCore import *

__appname__ = "Ninth Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        btn = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Checkbox Value")

        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        self.setLayout(layout)
        self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)

    def dialogOpen(self):
        initValue = {"mainSpinBox": self.mainSpinBox.value(), "mainCheckBox": self.mainCheckBox.isChecked()}
        dialog = Dialog(initValue)
        if dialog.exec_():
            # run in case SLOT("accept()") : OK
            self.mainSpinBox.setValue(dialog.spinbox.value())
            self.mainCheckBox.setChecked(dialog.checkbox.isChecked())


class Dialog(QDialog):

    def __init__(self, initValue, parent=None):
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

        self.spinbox.setValue(initValue["mainSpinBox"])
        self.checkbox.setChecked(initValue["mainCheckBox"])

        self.connect(buttonOk, SIGNAL("clicked()"), SLOT("accept()"))
        self.connect(buttonCancel, SIGNAL("clicked()"), SLOT("reject()"))

    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinbox.value() > 5:
                raise GreaterThanFive, ("The SpinBox value cannot be greater than 5")
            elif self.spinbox.value() == 0:
                raise IsZero, ("The SpinBox value cannot be equal to 0")
            else:
                QDialog.accept(self)

        except GreaterThanFive, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinbox.selectAll()
            self.spinbox.setFocus()
            return

        except IsZero, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinbox.selectAll()
            self.spinbox.setFocus()
            return


def main():
    app = QApplication(sys.argv)
    form = Program()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()

