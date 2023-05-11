from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

text_text = ["Ну и зачем ты это сделал?? Попросил же не нажимать на кнопку! Ладно, давай ещё раз: не нажимай на кнопку",
"Ты опять?! Я же сказал не нажимай! Даю тебе ещё одну попытку и помни не нажимай на кнопку.",
"Ты издеваешся? Единственное, чего я тебя прошу, это не нажимать на кнопку! Неужели так сложно??",
"Нет, ну это уже наглость!! Чего ты этим хочешь добиться?",
"Всё, молодец, ты меня довёл! Я ухожу! Можешь тут нажимать сколько хочешь! Всё пока.",
"",
"",
"",
"Слушай, это уже серьёзно, у тебя что дел других нет? Просто перестань!",
"Если ты продолжишь, я закрою это окно.",
"Я тебя предупредил!",
"3",
"2",
"1",
"...",
"Подожди, что-то сломалось, никуда не уходи.",
"",
"Всё, починил! Так на чём я остановился? А да, я закрываю это окно.",
"3",
"2",
"1",
"...",
"Опять?!",
"Похоже мы тут застряли, ну в таком случае можешь мне рассказать зачем ты нажимал на кнопку.",
"Я жду.",
"Стоп, я же тебя не слышу.",
"Ой подожди, я понял почему у меня не получается закрыть окно.",
"Подожди секунду.",
"",
"Всё, теперь точно починил.",
"Я наконец-то могу от тебя избавиться!",
"Ты приходи ещё, я буду ждать, пока!",]
i = 0

def test():
    global i
    if i == len(text_text): exit()
    text.setText(text_text[i])
    i += 1

app = QApplication([])
win = QWidget()
win.move(180,150)
win.setStyleSheet('font-size:30px;color:lime;background:black')
win.resize(500, 700)

line2 = QHBoxLayout()
line = QVBoxLayout()

text = QLabel("Привет! Меня зовут Не Нажимай Кнопку, но ты можешь звать меня ННК и я прошу тебя не нажимать на кнопку.")
line.addWidget(text, alignment=Qt.AlignCenter)

random_btn = QPushButton("кнопка")
random_btn.setStyleSheet('''width:10px;height:100px;background:grey;''')
random_btn.clicked.connect(test)
line.addWidget(random_btn)

win.setLayout(line)
win.show()
app.exec()