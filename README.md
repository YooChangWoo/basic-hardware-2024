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

## 3일차
- 가상환경 만들기
    - python -m venv --system-site-packages env

- RELAY MODUL
    - NO (NORMALLY OPEN) : 개방 터미널
    - C (Common termianl) : 공통 터미널
    - NC (NORMALLY CLOSED) : 폐쇄 터미널
    - 사용방법 : 예를 들어 LED1, 2를 제어하는 경우, LED1에는 NC, COM을 연결하고 LED2에는 NO, COM을 연결합니다. 즉,COM은 공통단자입니다.

- ULN2003
    - 고전류 다윈 트랜지스터 배열
    - 주로 스텝 모터와 릴레이 같은 고전류 부하를 제어

- 스텝모터(28BYJ-48)
    - 회전 운동을 여러 개의 작은 스텝으로 나누에 제어 할 수 있는 전기 모터
    - 제어 방법
        - GPIO 핀을 ULN2003의 입력 핀(1~4)에 연결
        - ULN2003의 출력 핀 (10-13)을 스텝 모터의 4개 코일에 연결
        - ULN2003DML RHDXHD VLN(8)을 접지에 연결
        - ULN2003의 다이오드 공통 핀(9)을 전원 공급 장치의 양극에 연결

- FLASK
    - Python으로 작성된 마이크로 웹 프레임워크
    - 단순하고 유연한 구조를 제공
    - 개발자가 원하는 방식으로 프로젝트를 구성

    - 주요 기능
        - 라우팅 : URL과 이를 처리할 함수를 연결
        - 요청 처리 : GET, POST와 같은 HTTP 메서드를 처리
        - 세션 관리 : 클라이언트 세션을 쉽게 관리
        - 에러 처리 : 커스텀 에러 페이지를 정의

## 4일차
- FLASK
    - 웹페이지에 HTML로 ON/OFF 버튼 만든 후 LED 작동

- Picamera
    - 카메라와 버튼을 이용하여 버튼을 누르면 사진 촬영

- 7 segment
    - Rasberry Pi와 7세그먼트 디스플레이를 사용한 숫자 표시
    - 회로구성
        - 1. 7-segment 디스플레이 핀아웃
            - 7-segment 디스플레이에는 총 10개의 핀이 있습니다. 이 핀들은 각 세그먼트와 공통 단자에 연결됩니다.
        - 2. 브레드보드 연결
            - 브레드보드에 7-segment 디스플레이를 배치하고 점퍼 케이블을 사용하여 Raspberry Pi의 GPIO 핀에 연결
        3. 저항 연결
            - 각 세그먼트 핀과 라즈베리파이 GPIO 핀 사이에 저항(220Ω 또는 330Ω)을 연결합니다. 이는 과전류로부터 디스플레이를 보호하기 위함
    - 주의 사항
        - 회로 연결 시 반드시 전원을 꺼두고 작업
        - 저항을 사용하여 디스플레이를 보호
        - 코드 실행 중 오류가 발생하면 GPIO.cleanup()을 사용하여 GPIO 핀 설정을 초기화