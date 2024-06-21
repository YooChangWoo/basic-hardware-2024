#pir
import RPi.GPIO as GPIO
import time

pirPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)

try:
    while True:
        if GPIO.input(pirPin) == True:
            print("Detected")
            time.sleep(0.5)

except KeyboardInterrupt:
<<<<<<< HEAD
    GPIO.cleanup()
=======
    GPIO.cleanup()
>>>>>>> 09af5ee0d282e138b839ea12e278975905347edd
