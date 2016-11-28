# Building an alarm pop-up

import sys
from PySide.QtGui import *
from PySide.QtCore import *
import time

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"

    if len(sys.argv) < 2:
        raise ValueError

    hours, minutes = sys.argv[1].split(":")
    due = QTime(int(hours), int(minutes))

    if not due.isValid():
        raise ValueError

    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: Video2.py HH:MM [optional message]"  # 24 hour clock


while QTime.currentTime() < due:
    time.sleep(10)
    print("Going sleep for 10 seconds..")

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()

QTimer.singleShot(20000, app.quit)
app.exec_()


