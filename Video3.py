# Creating an expression evaluator

import sys
from PySide.QtGui import *
from PySide.QtCore import *
import math


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.textBrowser = QTextBrowser()
        self.lineEdit = QLineEdit("Type an expression and press Enter")
        self.lineEdit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.lineEdit)
        self.setLayout(layout)

        self.lineEdit.setFocus()

        self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineEdit.text()
            self.textBrowser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.textBrowser.append("<font color=red>%s is invalid</font>" % text)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
