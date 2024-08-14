from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QLineEdit
from instr import *
class Final_Win(QWidget):
    def __init__(self,exp):
        self.exp=exp
    def results(self):
        self.index=index
        if self.exp.age1>=15:
            if self.index>=15:
                return txt_res1
            elif self.index<15 and self.index>=11:
                return txt_res2
            elif self.index<11 and self.index>=6:
                return txt_res3
            elif self.index<6 and self.index>=0.5:
                return txt_res4
            elif self.index<0.5:
                return txt_res5
    def initUI(self):
        self.work_text=QLabel(txt_workheart+self.results())
        self.index_text=Qlabel(txt_index+str(self.index))
app=QApplication([])
mw=Final_Win()
app.exec_()

