import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [130, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
    while True:
        x = input('1~8 사이 숫자를 입력하세요: ')
        Buzz.start(50)
        if x == '1':
            Buzz.ChangeFrequency(melody[0])
        elif x == '2':
            Buzz.ChangeFrequency(melody[1])
        elif x == '3':
            Buzz.ChangeFrequency(melody[2])
        elif x == '4':
            Buzz.ChangeFrequency(melody[3])
        elif x == '5':
            Buzz.ChangeFrequency(melody[4])
        elif x == '6':
            Buzz.ChangeFrequency(melody[5])
        elif x == '7':
            Buzz.ChangeFrequency(melody[6])
        elif x == '8':
            Buzz.ChangeFrequency(melody[7])

except KeyboardInterrupt:
    GPIO.cleanup()
