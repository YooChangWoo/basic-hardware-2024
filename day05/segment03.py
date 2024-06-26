import RPi.GPIO as GPIO
import time

# 세그먼트 핀 설정 (각 세그먼트 a, b, c, d, e, f, g에 연결된 핀 번호)
segments = (21, 23, 24, 19, 26, 20, 13)

# 각 자리수의 COM 핀 설정 (4자리)
com_pins = (25, 16, 18, 6)

# 숫자별 세그먼트 구성 (각 숫자에 대한 세그먼트의 ON/OFF 상태)
num = [
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)   # 9
]

# 버튼 핀 설정
button_pin = 12  # 버튼 핀을 12번으로 설정

# GPIO 설정
GPIO.setmode(GPIO.BCM)
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

for com in com_pins:
    GPIO.setup(com, GPIO.OUT)
    GPIO.output(com, GPIO.HIGH)  # 초기화 시 COM 핀은 비활성화 상태

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 현재 숫자 (초기값: 1024)
current_number = 1024
initial_display = True  # 초기 숫자 1024 표시 여부

def display_number(number):
    # 숫자를 네 자리로 분리하여 각각의 자리수로 변환
    digits = [int(d) for d in str(number).zfill(4)]
    for i in range(4):
        # 모든 COM 핀을 비활성화
        for com in com_pins:
            GPIO.output(com, GPIO.HIGH)
        
        # 세그먼트 핀 설정
        for j in range(7):
            GPIO.output(segments[j], num[digits[i]][j])
        
        # 해당 자리의 COM 핀 활성화
        GPIO.output(com_pins[i], GPIO.LOW)
        time.sleep(0.005)  # 약간의 지연을 줘서 눈에 보이게 함

try:
    # 초기 숫자 1024를 버튼 누르기 전까지 표시
    while initial_display:
        display_number(1024)
        if GPIO.input(button_pin) == GPIO.LOW:
            initial_display = False
            current_number = 0
            # 버튼 debounce를 위해 잠시 대기
            while GPIO.input(button_pin) == GPIO.LOW:
                time.sleep(0.01)  # 버튼이 눌린 상태가 끝날 때까지 대기
            time.sleep(0.2)  # 추가 debounce 대기

    while True:
        display_number(current_number)
        
        # 숫자가 자동으로 증가
        for i in range(10000):
            current_number = i
            start_time = time.time()
            while time.time() - start_time < 0.5:
                display_number(current_number)
            
            # 버튼이 눌린 경우 루프 탈출
            if GPIO.input(button_pin) == GPIO.LOW:
                break
        
        # 버튼 debounce를 위해 잠시 대기
        while GPIO.input(button_pin) == GPIO.LOW:
            time.sleep(0.01)  # 버튼이 눌린 상태가 끝날 때까지 대기
        time.sleep(0.6)  # 추가 debounce 대기
except KeyboardInterrupt:
    GPIO.cleanup()
