import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Rapport import Ui_MainWindowRapport

from PyQt5.QtWidgets import QMessageBox


class Rapport(QtWidgets.QMainWindow, Ui_MainWindowRapport):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

# SEARCH BUTTON "SEARCH ITEM IN FILE.TXT ANT PRINT IN LISTWIDGET"
        self.Search_btn.clicked.connect(self.search_click)

    def search_click(self):
        self.list_Purchas.clear()
        
        if self.Product.text() + self.Client.text() == '':

            msg = QMessageBox()
            msg.setWindowTitle("Attention")
            msg .setText("Input empty")
            msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

            return

        product_found = False

        with open("ListofPurchasing.txt", "r") as file_data:
            lines = file_data.readlines()

            for line in lines:
                if self.Product.text() + self.Client.text() in line:
                    product_found = True

                    item = line.strip()
                    self.list_Purchas.addItem(item)
                    
            if product_found == True:
                print("Product Found")
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Attention")
                msg .setText("Not Found")
                msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec_()
           
        file_data.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Rapport()
    main_window.show()
    sys.exit(app.exec_())
