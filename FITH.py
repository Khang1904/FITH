from PyQt6.QtWidgets import *
from PyQt6.uic import *
from random import randint, choice
import sys
import time



class Main(QDialog):
    def __init__(self,score):
        super(Main,self).__init__()
        loadUi("FITH.ui",self)
        self.setWindowTitle("Geometry Dash rng")
        self.mainBtn.clicked.connect(self.mainFunc)
        self.stars.display(score)

    def mainFunc(self):
        stars = randint(0,10)

        #Handles LOGS
        extls = ["N/A","Auto","Easy","Normal","Hard","Hard","Harder","Harder","Insane","Insane","Demon"]
        ext = extls[stars]
        if stars == 10:
            demon = choice(["Easy","Medium","Hard","Insane","Extreme"])
            self.lvlLog.addItem(f"+10 stars: {demon} Demon!")
        else:
            self.lvlLog.addItem(f"+{stars} stars: {ext}")

        #Handles LCD
        current = self.stars.value()
        self.stars.display(current+stars)
        current = self.stars.value()
        if current >= 65535:
            self.stars.display(65535)
            QMessageBox.information(self,"Maxed out!!!",'''You maxed out!
            Press OK to replay''')
            time.sleep(5)
            self.stars.display(0)

try:
    numls = []

    with open("score.txt","r") as f:
        content = f.read()
        digit_count = 0
        for char in content:
            if char.isdigit():
                digit_count += 1
                if digit_count >= 51:
                    numls.append(char)
        number = int("".join(map(str,numls)))
except:
    number = 0



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main(number)
    window.show()
    app.exec()


with open("score.txt","w") as f:
    towrite = ""
    for i in range(50):
        towrite += str(randint(0,9))
    towrite += str(window.stars.intValue())
    f.write(towrite)
