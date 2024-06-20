import RPi.GPIO as GPIO
import time

led = 21
blue = 20
green = 16
switch = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 내부 풀다운 저항 사용

def change_color():
    global led_on
    if led_on == 0:
        GPIO.output(led, True)
        GPIO.output(blue, False)
        GPIO.output(green, True)
    elif led_on == 1:
        GPIO.output(led, True)
        GPIO.output(blue, True)
        GPIO.output(green, False)
    else:
        GPIO.output(led, False)
        GPIO.output(blue, True)
        GPIO.output(green, True)

try:
    led_on = 0
    while True:
        if GPIO.input(switch) == GPIO.HIGH:
            led_on = (led_on + 1) % 3
            change_color()
            print("Switch pressed")
            time.sleep(0.3)  # 디바운싱을 위한 짧은 딜레이

except KeyboardInterrupt:
    GPIO.cleanup()
