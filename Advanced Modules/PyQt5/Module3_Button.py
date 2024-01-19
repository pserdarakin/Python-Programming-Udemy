import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)


    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle('PyQt5 Ders3')

    buton = QtWidgets.QPushButton(pencere)
    buton.setText('Burası Bir Butondur xd')
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText('Merhaba Dünya')

    buton.move(150,50)
    etiket.move(170,30)



    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()

