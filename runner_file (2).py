from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QGridLayout
from random import choice


app = QApplication([])


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.allmoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.yutish_shartlari = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [2, 5, 8],
            [1, 4, 7],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]
        self.xlar = []
        self.ylar = []
        self.btns = []
        self.flag = True
        a = QGridLayout()
        btn1 = QPushButton("")
        btn2 = QPushButton("")
        btn3 = QPushButton("")
        btn4 = QPushButton("")
        btn5 = QPushButton("")
        btn6 = QPushButton("")
        btn7 = QPushButton("")
        btn8 = QPushButton("")
        btn9 = QPushButton("")
        reset_btn = QPushButton("RESET ♻️")
        reset_btn.clicked.connect(self.reset_btn_clicked)
        reset_btn.setFixedSize(200, 80)
        reset_btn.setStyleSheet("background-color:green")
        font = QFont()
        font.setPointSize(50)

        # Set the font to the QLabel

        self.btns = [btn1, btn2,
                     btn3, btn4, btn5,
                     btn6, btn7, btn8, btn9]
        for i in range(len(self.btns)):
            self.btns[i].setFont(font)
            self.btns[i].setFixedSize(230, 230)
            self.btns[i].clicked.connect(self.btn_clicked)
            self.btns[i].setObjectName(f"{i + 1}")

        a.addWidget(btn1, 0, 0)
        a.addWidget(btn2, 0, 1)
        a.addWidget(btn3, 0, 2)
        a.addWidget(btn4, 1, 0)
        a.addWidget(btn5, 1, 1)
        a.addWidget(btn6, 1, 2)
        a.addWidget(btn7, 2, 0)
        a.addWidget(btn8, 2, 1)
        a.addWidget(btn9, 2, 2)
        a.addWidget(reset_btn, 3, 1)
        w = QWidget()
        w.setLayout(a)
        self.setCentralWidget(w)

    def btn_clicked(self):
        print(self.flag)
        if len(self.allmoves) == 0:
            return
        if self.flag:
            btn = self.sender()
            btn.setText("X")
            self.xlar.append(int(self.sender().objectName()))
            self.allmoves.remove(int(self.sender().objectName()))
            self.toggle()
            btn.setEnabled(False)
            print(self.sender().objectName())
            self.check()
            self.btn_clicked()
        else:
            a = choice(self.allmoves)
            self.allmoves.remove(a)
            btn = self.findChild(QPushButton, str(a))
            btn.setText("0")
            self.toggle()
            btn.setEnabled(False)
            self.ylar.append(a)
            print(a)
            self.check()


    def reset_btn_clicked(self):
        for i in range(len(self.btns)):
            self.btns[i].setEnabled(True)
            self.btns[i].setText("")
            self.btns[i].setStyleSheet("background-color: white")
        self.xlar.clear()
        self.ylar.clear()
        self.flag = True
        self.allmoves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def toggle(self):
        self.flag = not self.flag

    def check(self):
        for i in self.yutish_shartlari:
            if set(i).issubset(set(self.xlar)) or set(i).issubset(set(self.ylar)):
                self.disable()
                for j in i:
                    found_button = self.findChild(QPushButton, str(j))
                    found_button.setStyleSheet("background-color:green")

    def disable(self):
        for i in range(len(self.btns)):
            self.btns[i].setEnabled(False)
            # self.btns[i].setText("")


if __name__ == "__main__":
    wind = GameWindow()
    wind.show()
    app.exec()
