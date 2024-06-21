# basic-hardware-2024
2024년 IoT개발자과정 오픈하드웨어 플랫폼활용 리포지토리

## 1일차
- 옴의 법칙
    - 두 지점 간의 전압차, 두 지점 간에 흐르는 전류, 전류 경로의 저항은 모두 비례 V = IR
    - 전류 : I
    - 전압 : V
    - 저항 : R
- 키르히호프법칙
    - KCL
        - 전기 회로의 임의의 절점에 대해서 절점으로 흘러들어오는 전류의 총합과 흘러나가는 전류의 총합은 같습니다. (모든 총합은 0이 됩니다.)
    - KVL
        - 전기 회로의 임의의 닫힌회로에서 전압의 방향을 한 방향으로 했을 때 각 구간의 전압 상승의 총합과 전압 강하의 총합은 같습니다. (모든 총합은 0이 됩니다.)

- Python GPIO 설정함수
    - GPIO.setmode(GPIO.BOOARD) - wPi
    - GPIO.setmode(GPIO.BCM) - BCM
    - GPIO.setup(channel, GPIO.mode) - channel: 핀번호, mode: IN/OUT
    - GPIO.cleanup()
- GPIO 출력함수
    - GPIO.output(channel, state) - channel: 핀번호, state: HIGH/LOW or 1/0 or True/False
- GPIO 입력함수
    - GPIO.input(channel) - channel: 핀번호, 반환값: H/L or 1/0 or T/F
- 시간지연 함수
    - time.sleep(secs)
- GPIO 제어
    - LED, PWM, swich

## 2일차
- pir센서 활용
    - pir센서를 이용하여 led제어
- 초음파 거리 센서
    - 초음파 거리 센서를 이용하여 부저 제어
