from PyQt5.QtWidgets import QApplication,QDialog,QProgressBar,QVBoxLayout,QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QThread,pyqtSignal
import time



class Window(QDialog):
    def __init__(self): # 폼 구성
        super().__init__()
        self.title = "PYQT5 Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100
        # self.iconName = "SEO.png"
        self.setWindowTitle(self.title)
        # self.setWindowIcon(self.iconName)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()  # 초기 UI 화면 구성 불러오기
        self.show()

    def InitUI(self): # 폼에 들어갈 항목들 구성
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("run progressbar") # 버튼 추가
        self.button.clicked.connect(self.startProgressBar)  # 버튼 클릭하면 프로그래스바 함수 스타트
        vbox.addWidget(self.button)
        self.setLayout(vbox)

    def startProgressBar(self):  # 프로그래스바 시작
        self.thread = MyThread()  # MyThread 클레스 선언
        # MytThread에서 사용한 change_value라는 pyqtSignal을 받아서 연결해준다
        self.thread.change_value.connect(self.setProgressVal) # change_value값이날라오면 연결한다 setProgressvVal 함수에 전달한다
        self.thread.start() # 쓰레드 실행

    def setProgressVal(self,Val): # Val값을 받아서 Progressbar를 업데이트 한다
        self.progressbar.setValue(Val) # setProgressVal 함수 선언 Val를 전달 받아서 progessbar의 Setvalu를 Val로 입력

class MyThread(QThread): # Qthread  실제 실행하고자 하는 함수 !!!!
    change_value = pyqtSignal(int) # 시크널을 change_value 라는 변수에 담아서 보내준다
    def run(self):
        cnt = 0
        while cnt < 100:
            cnt+=1
            time.sleep(0.3)
            self.change_value.emit(cnt) # change_valu 값을 방출한다. cnt를 담아서
            print("카운트:", cnt)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

