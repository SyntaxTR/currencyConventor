import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

from assets.python.designer import Ui_KurHesaplayici
from assets.python.functions import MyFunctions

from threading import Timer
import datetime

class initUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_KurHesaplayici()
        self.ui.setupUi(self)

        self.reloadCurrencys()
        self.ui.pushButton.clicked.connect(self.Calculate)

    def reloadCurrencys(self):
        print("Güncellendi:" + str(datetime.datetime.now()))
        self.Functions = MyFunctions()
        
        self.ui.label_2.setText("<html><head/><body><p><span style=\" font-size:12pt;\">Dolar: "+ self.Functions.Dolar +"</span></p></body></html>")
        self.ui.label_3.setText("<html><head/><body><p><span style=\" font-size:12pt;\">Euro: "+ self.Functions.Euro +"</span></p></body></html>")
        self.ui.label_4.setText("<html><head/><body><p><span style=\" font-size:12pt;\">Gram Altın: "+ self.Functions.Altin +"</span></p></body></html>")
        self.ui.label_8.setText("<html><head/><body><p><span style=\" font-size:12pt;\">Gümüş: "+ self.Functions.Gumus +"</span></p></body></html>")
      

    def getSelectedRadioButtonValue(self,whichGroup):
        result = 1
        obj = self.ui.splitter if (whichGroup == 1) else self.ui.splitter_2
        for i in obj.findChildren(QtWidgets.QRadioButton):
            if(i.isChecked()):
                buttonText = i.text()
                if(buttonText == "Gram Altın"):
                    result = self.Functions.Altin
                elif(buttonText == "Dolar"):
                    result = self.Functions.Dolar   
                elif(buttonText == "Euro"):
                    result = self.Functions.Euro
                elif(buttonText == "Gümüş"):
                    result = self.Functions.Gumus   
                elif(buttonText == "TL"):
                    result = 1  
        return result                              


    def Calculate(self):
        miktar = self.Functions.str2Num(self.ui.lineEdit.text())
        if(type(miktar) != int and type(miktar) != float):
            print("Sadece rakam giriniz")
        else:
            group_0 = self.getSelectedRadioButtonValue(1)
            group_1 = self.getSelectedRadioButtonValue(2)

            sonuc = str( round( ((miktar * float(group_0))) / float(group_1), 3))

            self.ui.label_7.setText("<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Sonuç: "+ sonuc +"</span></p></body></html>")
            



def startUI():
    app = QApplication(sys.argv)
    main = initUI(); 
    main.show()
    sys.exit(app.exec_())

startUI()    