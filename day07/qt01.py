import sys
form PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test01.ui")[0]

# sindowClass
class WindowClass(QMainWindow, form_class):
	def __init__(self):      # 생성자, 첫번째인자는 self
		super().__init()__()   # 부모클래스생성자(QWidges)
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv) # 애플리케이션 실행코드
	myWindow = WindowClass()     # WindowClass() 인스턴스 생성
	myWindow.show()              # 화면 보여주기
	app.exec_()                  # 이벤트 루프 실행
