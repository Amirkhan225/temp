<<<<<<< HEAD
=======
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton
from instr import *
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
txt_title = 'Здоровье'
txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = ('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                    'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                    'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                    'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                    'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                    'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                    'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                    'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )
class Main_Win(Qwidget):
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
            self.hello_text=QLabel(txt_hello)
            self.instruction=Qlabel(txt_instruction)
            self.button=QPushButton(txt_next)
            self.layout=QVBoxLayout()
            self.layout.addWidget(self.hello_text)
            self.layout.addWidget(self.instruction)
            self.layout.addWidget(self.button)
        def connects(self):
            self.btn_next.clicked.connect(self.next_click)
        def next_click(self):
            self.hide()
            self.tw=WinTwo
app=QApplication([])
mw=Main_Win()
app.exec_()
>>>>>>> b50d0e42e29463c7c774c673a42b07e89083d020
