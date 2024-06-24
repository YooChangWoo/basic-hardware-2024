# URL접속을 /led/on, /led /off 로 접속하면 led를 on, off하는 웹페이지를 만들자

from flask import Flask
import RPi.GPIO as GPIO

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)

@app.route("/led/on")
def led_on():
	GPIO.output(led, False)
	return "led on!!!"

@app.route("/led/off")
def led_off():
	GPIO.output(led, True)
	return "led off!!!"

if __name__ =="__main__":
	try:
		while True:
			app.run(host="0.0.0.0", port="10011", debug=True)

	except KeyBoardInterrupt:
		GPIO.cleanup()
