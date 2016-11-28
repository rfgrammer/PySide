# Events explained

import sys
from PySide.QtGui import *
from PySide.QtCore import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dial = QDial()
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)

        self.setWindowTitle("Signals and Slots")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()


