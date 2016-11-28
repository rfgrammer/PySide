# PyDataManager exercise

from PySide.QtCore import *
from PySide.QtGui import *
from ui_files import mainGui
import sys
import os
import logging
import sqlite3
import utilities
import about
import preferences
import re
import csv

__appname__ = "PyDataMan"
__module__ = "main"

appDataPath = os.environ["APPDATA"] + "\PyDataMan\\"

if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception, e:
        appDataPath = os.getcwd()

logging.basicConfig(filename=appDataPath + "pydataman.log",
                    format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s %(lineno)-6d %(message)s")

logger = logging.getLogger(name="main-gui")


class MainWindow(QMainWindow, mainGui.Ui_MainWindow):

    dbPath = appDataPath + "pydata.db"
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Main(id INTEGER PRIMARY KEY,
                                 username TEXT, name TEXT, phone TEXT, address TEXT, status TEXT)""")

        self.dbConn.commit()

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "PyDataMan")

        self.addData.clicked.connect(self.add_button_clicked)
        self.removeRow.clicked.connect(self.remove_row_button_clicked)
        self.actionImport.triggered.connect(self.import_action_triggered)
        self.actionExport.triggered.connect(self.export_action_triggered)
        self.actionPreference.triggered.connect(self.preferences_action_triggered)
        self.actionExit.triggered.connect(self.exit_action_triggered)
        self.actionAbout.triggered.connect(self.about_action_triggered)

        self.showToolbar = utilities.str2bool(self.settings.value("showToolbar", True))
        self.toolBar.setVisible(self.showToolbar)

        self.load_initial_settings()

    def load_initial_settings(self):
        """Loads the initial settings for the application. Sets the mainTable column widths,"""

        self.dbCursor.execute("""SELECT * FROM Main""")
        allRows = self.dbCursor.fetchall()

        for row in allRows:
            idx = allRows.index(row)
            self.mainTable.insertRow(idx)
            self.mainTable.setItem(idx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(idx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(idx, 2, QTableWidgetItem(row[3]))
            self.mainTable.setItem(idx, 3, QTableWidgetItem(row[4]))
            self.mainTable.setItem(idx, 4, QTableWidgetItem(row[5]))

    def validate_fields(self):
        """Validates the QLineEdits based on RegEx"""

        self.dbCursor.execute("""SELECT username FROM Main""")
        usernames = self.dbCursor.fetchall()
        for username in usernames:
            if self.userName.text() in username[0]:
                QMessageBox.warning(self, "Warning", "Such username already exists!")
                return False

        if not re.match('^[2-9]\d{2}-\d{3}-\d{4}', self.phoneNumber.text()):
            QMessageBox.warning(self, "Warning", "Phone number seems incorrect!")
            return False
        return True

    def add_button_clicked(self):
        """Calls the validate_fields() method and adds the items to the table if true"""

        username = self.userName.text()
        first_name = self.firstName.text()
        phone = self.phoneNumber.text()
        address = self.address.text()
        approved = self.approved.isChecked()

        if not self.validate_fields():
            return False

        currentRowCount = self.mainTable.rowCount()

        self.mainTable.insertRow(currentRowCount)
        self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(username))
        self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(first_name))
        self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(phone))
        self.mainTable.setItem(currentRowCount, 3, QTableWidgetItem(address))
        self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem("Approved" if approved else "Not approved"))

        parameters = (None, username, first_name, phone, address, str(approved))
        self.dbCursor.execute('''INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?)''', parameters)
        self.dbConn.commit()

    def remove_row_button_clicked(self):
        currentRow = self.mainTable.currentRow()

        if currentRow > -1:
            currentUsername = (self.mainTable.item(currentRow, 0).text(),)
            self.dbCursor.execute("""DELETE FROM Main WHERE username=?""", currentUsername)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)

    def about_action_triggered(self):
        dlg = about.About()
        dlg.show()
        dlg.exec_()

    def import_action_triggered(self):
        """Database import handler"""
        # THIS IS HOMEWORK! Hint #1 - Read the python doc csv.reader ; Hint #2 - There's nothing new here.
        pass

    def export_action_triggered(self):
        """Database export handler"""

        self.dbCursor.execute("""SELECT * FROM Main""")

        dbFile = QFileDialog.getSaveFileName(parent=None, caption="Export database to a file", directory=".", filter="PyDataMan CSV (*.csv)")

        if dbFile[0]:
            try:
                with open(dbFile[0], "wb") as csvFile:
                    csvWriter = csv.writer(csvFile, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)

                    rows = self.dbCursor.fetchall()
                    rowCount = len(rows)

                    for row in rows:
                        csvWriter.writerow(row)

                    QMessageBox.information(self, __appname__, "Successfully exported " + str(rowCount) + " rows to a file\r\n" + str(QDir.toNativeSeparators(dbFile[0])))
            except Exception, e:
                QMessageBox.critical(self, __appname__, "Error exporting file, error is\r\n" + str(e))
                return

    def preferences_action_triggered(self):
        """Fires up the Preferences dialog"""

        dlg = preferences.Preferences(self, showToolbar=self.showToolbar)
        sig = dlg.checkboxSig

        sig.connect(self.showHideToolbar)
        dlg.exec_()

    def showHideToolbar(self, param):
        """Shows/hides main toolbar based on the checkbox value from preferences"""

        self.toolBar.setVisible(param)
        self.settings.setValue("showToolbar", utilities.bool2str(param))

    def exit_action_triggered(self):
        self.close()

    def closeEvent(self, event, *args, **kwargs):
        """Overwrite the default close method"""

        result = QMessageBox.question(self, __appname__, "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    QCoreApplication.setApplicationName("PyDataMan")
    QCoreApplication.setApplicationVersion("0.1")
    QCoreApplication.setOrganizationName("PyDataMan")
    QCoreApplication.setOrganizationDomain("pydataman.com")

    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()

