import RPi.GPIO as GPIO
import time

# 세그먼트 핀 설정 (각 세그먼트 a, b, c, d, e, f, g에 연결된 핀 번호)
segments = (21, 23, 24, 19, 26, 20, 13)

# 숫자별 세그먼트 구성 (각 숫자에 대한 세그먼트의 ON/OFF 상태)
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

# 버튼 핀 설정
button_pin = 12
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 현재 숫자
current_number = 0

def display_number(number):
    for i in range(7):
        GPIO.output(segments[i], num[number][i])

try:
    display_number(current_number)  # 초기 숫자 디스플레이
    while True:
        # 버튼이 눌렸는지 확인
        if GPIO.input(button_pin) == GPIO.LOW:
            # 숫자를 하나 증가시킴
            current_number = (current_number + 1) % 10
            display_number(current_number)
            print(f"Current number: {current_number}")
            # 버튼 debounce를 위해 잠시 대기
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.01)  # 버튼이 눌린 상태가 끝날 때까지 대기
            time.sleep(0.2)  # 추가 debounce 대기
except KeyboardInterrupt:
    GPIO.cleanup()
