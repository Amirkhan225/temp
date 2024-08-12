from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QLineEdit
from instr import *

class Test_Win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.name=QLabel('Введите Ф.И.О.:')
        self.age=QLabel('Полных лет:')
        self.description1=QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.description2=QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
        self.description3=QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.text_timer=QLabel('hh:mm:ss')
        
        self.test1=QPushButton('Начать первый тест')
        self.training=QPushButton('Начать делать приседания')
        self.f_test=QPushButton('Начать финальный тест')
        self.result=QPushButton('Отправить результаты')
        self.name1=QLineEdit('Ф.И.О.')
        self.age1=QLineEdit('0')
        self.pulse1=QLineEdit('0')
        self.pulse2=QLineEdit('0')
        self.pulse3=QLineEdit('0')
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.l_line.addWidget(self.name,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.name1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age,alignment=Qt.AlignLeft)          
        self.l_line.addWidget(self.age1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.description1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.description2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.training,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.description3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.f_test,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.pulse3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.result,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()
    def timer_sits(self):
        global time
        time=QTime(0,0,30)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer3Event(self):
        global time
        time=time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times",36,QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if int(time.toString("hh:mm:ss")[6:8])>=45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8])<=15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif time.toString("hh:mm:ss")=="00:00:00":
            self.timer.stop()
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
    def timer_final(self):
        global time
        time=QTime(0,1,0)
        self.timer=QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def connects(self):
        self.result.clicked.connect(self.next_click)
        self.test1.clicked.connect(self.timer_test)
        self.training.clicked.connect(self.timer_sits)
        self.f_test.clicked.connect(self.timer_final)
    def next_click(self):
        self.hide()
        self.tw=WinThree()
        #fix

if __name__ == "__main__":
    
    app=QApplication([])
    mw=Test_Win()
    app.exec_()
