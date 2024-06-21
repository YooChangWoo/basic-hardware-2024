# Ultra
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigerPin, True)  ## 10us 동안 high레벨로 triger출력하여 초음 발생준비
	time.sleep(0.00001)
	GPIO.output(trigerPin, False)
	start = time.time()            # 현재 시간 저장

	while GPIO.input(echoPin) == False:  # echo가 없으면
		stop = time.time()								 # 현재 시간을 start변수에 저장하고
	while GPIO.input(echoPin) == True:	 # echo 가 있으면
		stop = time.time()								 # 현재시간을 stop변수에 저장
		elapsed = stop - start						 # 걸린 시간을 구하고
		distance = (dlapsed * 19000) / 2	 # 초음파속도를 이용해서 거리계산

		return distance										 # 거리반환

# 핀설정
triperPin = 27 
echoPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO)
GPIO.setup(echoPin, GPIO)

try:
	while True:
		distance = measure():
		print("Diatance: %.2f c"'%distance)
		time.sleep()

except KeyboardInterrupt:
	GPIO.cleanup
