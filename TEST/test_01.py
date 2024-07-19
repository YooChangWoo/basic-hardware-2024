from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer
import RPi.GPIO as GPIO
import time
import sys
import os

# 환경 변수 설정
os.environ['QT_QPA_PLATFORM'] = 'offscreen'

# UI 파일을 로드합니다.
form_class = uic.loadUiType("./project.ui")[0]

# GPIO 설정
led_red = 17
led_blue = 22
led_green = 4
piezoPin = 13
trigPin = 20
echoPin = 16

# GPIO 경고 비활성화
GPIO.setwarnings(False)

# GPIO 모드 설정
GPIO.setmode(GPIO.BCM)

# 부저 설정
GPIO.setup(piezoPin, GPIO.OUT)
Buzz = GPIO.PWM(piezoPin, 440)

# 초음파 센서 설정
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

# LED GPIO 설정
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)

# 초기 LED 상태 설정 (모두 끔)
GPIO.output(led_red, True)
GPIO.output(led_blue, True)
GPIO.output(led_green, True)

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blinkLEDs)
        self.light_btn_on.clicked.connect(self.btn1Function)
        self.light_btn_off.clicked.connect(self.btn2Function)
        self.buzzer_on.clicked.connect(self.buzzerOnFunction)
        self.buzzer_off.clicked.connect(self.buzzerOffFunction)
        self.ultra_on.clicked.connect(self.ultraOnFunction)
        self.ultra_off.clicked.connect(self.ultraOffFunction)

        self.running = False
        self.blink_state = 0

    def btn1Function(self):
        self.running = True
        self.timer.start(1000)  # 1초마다 타이머 실행

    def btn2Function(self):
        self.running = False
        self.timer.stop()
        GPIO.output(led_red, False)  # LED 끄기
        GPIO.output(led_blue, False)  # LED 끄기
        GPIO.output(led_green, False)  # LED 끄기
        self.LedText.setText("LED OFF")

    def blinkLEDs(self):
        if self.running:
            if self.blink_state == 0:
                GPIO.output(led_red, True)
                GPIO.output(led_blue, False)
                GPIO.output(led_green, True)
                self.blink_state = 1
            elif self.blink_state == 1:
                GPIO.output(led_red, True)
                GPIO.output(led_blue, True)
                GPIO.output(led_green, False)
                self.blink_state = 2
            else:
                GPIO.output(led_red, False)
                GPIO.output(led_blue, True)
                GPIO.output(led_green, True)
                self.blink_state = 0

    def buzzerOnFunction(self):
        Buzz.start(50)
        self.BuzText.setText("BUZ ON")

    def buzzerOffFunction(self):
        Buzz.stop()
        self.BuzText.setText("BUZ OFF")

    def slot1(self):
        GPIO.cleanup()
        myWindow.close()
        print("EXIT!!")

    def ultraOnFunction(self):
        GPIO.output(trigPin, True)
        time.sleep(0.00001)
        GPIO.output(trigPin, False)
        start = time.time()

        while GPIO.input(echoPin) == False:
            start = time.time()
        while GPIO.input(echoPin) == True:
            stop = time.time()
        elapsed = stop - start
        distance = (elapsed * 34300) / 2

        self.lcdNumber.display(distance)
        self.timer.start(500)

    def ultraOffFunction(self):
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
