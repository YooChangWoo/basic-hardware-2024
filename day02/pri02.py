import RPi.GPIO as GPIO
import time

led = 21
priPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(priPin, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

try:
<<<<<<< HEAD
  while True:
    if GPIO.input(priPin) == False:
      if GPIO.input(led) == False:
        print("Detected")
        time.sleep(0.5)

    else:
      GPIO.OUT(led)==True:
        print("NO Detected")
=======
    while True:
        if GPIO.input(priPin) == True:
            GPIO.output(led, False)
            print("Detected")
        else:
            GPIO.output(led, True)
            print("NO Detected")
>>>>>>> 09af5ee0d282e138b839ea12e278975905347edd
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
<<<<<<< HEAD


try:
   while True:
      distance = measure()
      print("Distance: %2.f cm" %distance)
      if distance <= 50:
         Buzz.start(50)
         delay = distance / 100
         time.sleep(delay)
         Buzz.stop()
         time.sleep(delay)
      else:
         Buzz.stop()
         time.sleep(0.1)
=======
>>>>>>> 09af5ee0d282e138b839ea12e278975905347edd
