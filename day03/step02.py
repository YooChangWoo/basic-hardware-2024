import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
steps = [21, 22, 23, 24]

for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT)
	GPIO.output(stepPin, 0)


Sequence = [
	[0,0,0,1],
	[0,0,1,0],
	[0,1,0,0],
	[1,0,0,0]
]
try:
	while True:
		for step in Sequence:
			for pin in range(len(steps)):
				GPIO.output(steps[pin], step[pin])
			time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
