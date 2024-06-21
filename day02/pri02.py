import RPi.GPIO as GPIO
import time

led = 21
priPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(priPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        if GPIO.input(priPin) == True:
            GPIO.output(led, False)
            print("Detected")
        else:
            GPIO.output(led, True)
            print("NO Detected")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
