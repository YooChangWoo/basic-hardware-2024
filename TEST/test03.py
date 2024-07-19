import RPi.GPIO as GPIO
import time
import sys
import adafruit_dht
import board
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
from picamera2 import Picamera2
from PyQt5.QtGui import QPixmap

# UI 파일을 로드합니다.
form_class = uic.loadUiType("./project.ui")[0]

# GPIO 설정
led_red = 17
led_blue = 22
led_green = 4
piezoPin = 27
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

# 카메라 설정
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

# stepPin 변수를 정의
steps = [5, 6, 13, 19]

# GPIO 핀 설정
for stepPin in steps:
    GPIO.setup(stepPin, GPIO.OUT)
    GPIO.output(stepPin, 0)

class LEDThread(QThread):
    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        while self.running:
            GPIO.output(led_red, True)
            GPIO.output(led_blue, False)
            GPIO.output(led_green, True)
            time.sleep(1)
            GPIO.output(led_red, True)
            GPIO.output(led_blue, True)
            GPIO.output(led_green, False)
            time.sleep(1)
            GPIO.output(led_red, False)
            GPIO.output(led_blue, True)
            GPIO.output(led_green, True)
            time.sleep(1)

    def stop(self):
        self.running = False
        self.wait()

class MotorThread(QThread):
    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        Sequence = [
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0]
        ]
        while self.running:
            for step in Sequence:
                for pin in range(len(steps)):
                    GPIO.output(steps[pin], step[pin])
                time.sleep(0.01)

    def stop(self):
        self.running = False
        self.wait()

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.ultraOnFunction)

        # 이벤트 함수 연결
        self.light_btn_on.clicked.connect(self.btn1Function)
        self.light_btn_off.clicked.connect(self.btn2Function)
        self.spk_btn_on.clicked.connect(self.buzzerOnFunction)
        self.spk_btn_off.clicked.connect(self.buzzerOffFunction)
        self.pir_btn_on.clicked.connect(self.ultraOnFunction)
        self.pir_btn_off.clicked.connect(self.ultraOffFunction)
        self.cmr_btn.clicked.connect(self.cameraFunction)
        self.motor_btn_on.clicked.connect(self.stepOnFunction)
        self.motor_btn_off.clicked.connect(self.stepOffFunction)

        self.led_thread = LEDThread()
        self.motor_thread = MotorThread()

    def btn1Function(self):
        self.led_thread.running = True
        self.led_thread.start()

    def btn2Function(self):
        self.led_thread.stop()
        GPIO.output(led_red, True)
        GPIO.output(led_blue, True)
        GPIO.output(led_green, True)
        self.LedText.setText("LED OFF")

    def buzzerOnFunction(self):
        Buzz.start(50)

    def buzzerOffFunction(self):
        Buzz.stop()

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
        distance = (elapsed * 19000) / 2
        print(distance)
        self.timer.start(500)

    def ultraOffFunction(self):
        self.timer.stop()

    def cameraFunction(self):
        time.sleep(2)
        filename = "photo.jpg"
        picam2.capture_file(filename)
        pixmap = QPixmap(filename)
        self.photo_label.setPixmap(pixmap.scaled(self.photo_label.width(), self.photo_label.height(), Qt.KeepAspectRatio))

    def stepOnFunction(self):
        self.motor_thread.running = True
        self.motor_thread.start()

    def stepOffFunction(self):
        self.motor_thread.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
