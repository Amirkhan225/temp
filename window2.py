from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QLineEdit
from instr import *

class Test_Win(Qwidget):
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
            self.description3=Qlabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')
            self.timer=Qlabel('hh:mm:ss')
            time = QTime(0, 0, 15)
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
            self.r_line.addWidget(,alignment=Qt.AlignRight)
            self.h_line.addLayout(self.l_line)
            self.h_line.addLayout(self.r_line)
            
        def connects(self):
            self.btn_next1.clicked.connect(self.next_click)
        def next_click(self):
            self.hide()
            self.tw=WinTwo
app=QApplication([])
mw=Main_Win()
app.exec_()
