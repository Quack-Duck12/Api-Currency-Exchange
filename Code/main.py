from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from logic import *

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("Code\\UI\\Currency.ui",self)
        self.show()

        self.currentfile = ""

        self.ConvertButton.clicked.connect(self.Convert)
        self.actionRefresh.triggered.connect(self.Convert)
        self.actionExit.triggered.connect(self.Exit)

    def Convert(self):

        Amt = self.Amtbox.text()
        From = self.From.currentText()
        To = self.To.currentText()

        if Amt == '':
            Amt = 0

        Converted = Convert(Amt,From,To)

        self.Outbox.clear()
        self.Outbox.insertPlainText(f"{Converted}")

    def Exit(self):
        import sys
        sys.exit()


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()


if __name__ == "__main__":
    main()
