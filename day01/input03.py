import RPi.GPIO as GPIO

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

def turn_on_led():
    GPIO.output(led, False)

def turn_off_led():
    GPIO.output(led, True)

try:
    while True:
        user_input = input("Enter 'o' to turn on the LED, 'x' to turn it off: ")

        if user_input.lower() == 'o':
            turn_on_led()
            print("LED turned on")
        elif user_input.lower() == 'x':
            turn_off_led()
            print("LED turned off")
        else:
            print("Invalid input. Enter 'o' to turn on the LED, 'x' to turn it off.")

except KeyboardInterrupt:
    GPIO.cleanup()
