from flask import Flask
import RPi.GPIO as GPIO

led1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def led():
   return "Hello led!!"

@app.route("/led/<state>")
def led_on_off(state):
   if state == "on":
      GPIO.output(led1, False)
      return "led on!!"

   elif state == "off":
      GPIO.output(led1, True)
      return "led off!!"

   elif state == "clear":
      GPIO.cleanup()
      return "GPIO Cleanup()"

if __name__ == "__main__":
   app.run(host = "0.0.0.0", port = 10012, debug = True)

