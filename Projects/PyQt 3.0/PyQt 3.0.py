#presentation https://docs.google.com/presentation/d/14PsvFT_9wBGSXjAtZ1D0K909I5fUud2U4GPuVMDoypQ/edit#slide=id.g132709bd007_0_318

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
 