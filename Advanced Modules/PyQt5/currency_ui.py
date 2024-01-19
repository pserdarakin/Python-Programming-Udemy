import sys
import requests
import os


from PyQt5 import QtWidgets

class Döviz(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.baglan()
        self.init_ui()

    def init_ui(self):

        self.usd = QtWidgets.QLineEdit()
        self.cevir = QtWidgets.QPushButton('Çevir')
        self.sonuc = QtWidgets.QLabel('')

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.usd)
        v_box.addWidget(self.cevir)
        v_box.addWidget(self.sonuc)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()


        self.setLayout(h_box)
        self.setWindowTitle('Döviz Çevirici')
        self.cevir.clicked.connect(self.baglan)

        self.show()

    def baglan(self):
        api_key = "2aea0cd7887545a42810499fa7dea176"
        url = "http://data.fixer.io/api/latest?access_key=" + api_key
        first_currency = self.usd
        second_currency = url
        self.response = requests.get(url)

        self.bilgiler = response.json()

        self.fV = self.bilgiler['rates'][first_currency]
        self.sV = self.bilgiler['rates'][second_currency]

        self.baglan = (secondValue / firstValue) * amount

app = QtWidgets.QApplication(sys.argv)

pencere = Döviz()

sys.exit(app.exec_())

