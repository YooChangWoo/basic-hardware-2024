import RPi.GPIO as GPIO
import time

led = 21
blue = 20
green = 16
#GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)
#GPIO핀 설정(입력/출력)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

try:
  while True:
    GPIO.output(led, False)
    GPIO.output(blue, True)
    GPIO.output(green, True)
    time.sleep(1)
    GPIO.output(led, True)
    GPIO.output(blue, False)
    GPIO.output(green, True)
    time.sleep(1)
    GPIO.output(led, True)
    GPIO.output(blue, True)
    GPIO.output(green, False)
    time.sleep(1)

except KeyboardInterrupt:  #Ctrl + c
  GPIO.cleanup()
