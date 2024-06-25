import RPi.GPIO as GPIO
import time

a = 21
f = 20
b = 23
e = 26
d = 19
c = 24
g = 13

# 세그먼트 핀 설정 (각 세그먼트 a, b, c, d, e, f, g에 해당하는 GPIO 핀 번호)
segments = (21, 23, 24, 19, 26, 20, 13)

# 숫자별 세그먼트 구성 (각 숫자에 대한 세그먼트의 ON/OFF 상태를 정의)
num = [
    (1,1,1,1,1,1,0),  # 0
    (0,1,1,0,0,0,0),  # 1
    (1,1,0,1,1,0,1),  # 2
    (1,1,1,1,0,0,1),  # 3
    (0,1,1,0,0,1,1),  # 4
    (1,0,1,1,0,1,1),  # 5
    (1,0,1,1,1,1,1),  # 6
    (1,1,1,0,0,0,0),  # 7
    (1,1,1,1,1,1,1),  # 8
    (1,1,1,1,0,1,1)   # 9
]

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

try:
    while True:
        for digit in num:
            for i in range(7):
                GPIO.output(segments[i], digit[i])
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
