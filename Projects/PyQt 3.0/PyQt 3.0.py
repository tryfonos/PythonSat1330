from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys

class View(QMainWindow):
    
 


class Model():
    

class Controller(): 

app = QApplication(sys.argv)
key = 5
myModel = Model(key)
myController = Controller(myModel)
myView = View(myController)
myView.show()
sys.exit(app.exec_())
 