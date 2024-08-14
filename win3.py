from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QLineEdit
from instr import *



class Final_Win(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp=exp
        self.set_appear()
        self.initUI()
        self.results()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.layout=QVBoxLayout()
        self.work_text=QLabel(txt_workheart+self.results())
        self.index_text=QLabel(txt_index+str(self.index))
        self.layout.addWidget(self.index_text,alignment=Qt.AlignCenter)
        self.layout.addWidget(self.work_text,alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def results(self):
        self.index=(4*(self.exp.pulse1+self.exp.pulse2+self.exp.pulse3)-200)/10

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

