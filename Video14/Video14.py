import sys
import time

from PySide.QtCore import *
from PySide.QtGui import *

import showGui


class MainDialog(QDialog, showGui.Ui_mainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.showButton.setText("Process")
        self.connect(self.showButton, SIGNAL("clicked()"), self.processData)

        self.workerThread = WorkerThread()
        self.connect(self.workerThread, SIGNAL("threadDone(QString)"), self.threadDone, Qt.DirectConnection)

    def processData(self):
        self.workerThread.start()
        QMessageBox.information(self, "Done!", "Done.")

    def threadDone(self, text):
        self.nameEdit.setText("Worker thread finished processing.")
        print(text)


class WorkerThread(QThread):

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        time.sleep(5)
        self.emit(SIGNAL("threadDone(QString)"), "Confirmation that the thread is finished.")


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
