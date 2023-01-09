import pyautogui
import sys
# sys.exit()로 작업중단?
size = pyautogui.size() # 내 컴퓨터
pyautogui.sleep(1)
pyautogui.countdown(3)

    ## 위치확인 ##

p = pyautogui.position()
print(p[0], p[1]) #  =(p.x, p.y)
pyautogui.mouseInfo() # 색상도 확인가능

    ## 마우스 ##

pyautogui.moveTo(100,200) # 절대좌표
pyautogui.move(100,100, duration=0.25) # 상대좌표
for i in range(10): # 반복문 적용
    pyautogui.move(100,100)
    pyautogui.sleep(1)

pyautogui.click(64,17,duration=1) # duration은 이속
pyautogui.click(clicks=500) # 클릭 반복작업 횟수
pyautogui.rightClick() # 우클릭
pyautogui.drag(100,0,duration=0.25) # 드래그. 얘도 To붙이면 절대성
pyautogui.scroll(300) # (-300)이면 아래로 스크롤

    ## 스크린 이미지 ## [Win + Shift + S] / 속도개선법은 6번파일

img = pyautogui.screenshot()
img.save("shotimage.png")

file_menu = pyautogui.locateOnScreen("file_menu.png")
pyautogui.click(file_menu) # 중간부분에 에임
for i in pyautogui.locateAllOnScreen("checkbox.png"):
    pyautogui.click(i, duration=0.25) # 같은 거 다 체크

# 느리게 찾아도 계속 기다려줄게    
note_file_menu = pyautogui.locateOnScreen("note_file_menu.png")
while note_file_menu is None:
    note_file_menu = pyautogui.locateOnScreen("note_file_menu.png")
    print("발견 실패")
pyautogui.click(note_file_menu)
print("실행 완료")

# 속도개선 + 정확도 낮추기의 예시를 보여주면
btn_text = pyautogui.locateOnScreen("quiz_text.png", confidence=0.8) 
# 만약 항목을 찾지 못했을때 이렇게 하면 찾을 확률이 많이 올라가지.

    ## 윈도우 창 ##

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) 
print(fw.size) 
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보. 자동 꼭짓점
pyautogui.click(fw.left + 25 , fw.top + 20)
for w in pyautogui.getAllWindows():
    print(w) # 윈도우 활성화 다 가져오기
for w in pyautogui.getWindowsWithTitle("제목 없음"):
    print(w)
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
if w.isActive == False : # 현재 활성화가 되지 않았다면, 이라는 뜻인데 실험결과 있든없든 실행되는데...
    w.activate()
w.maximize() # 최대화 (.isMaximized)
w.minimize() # 최소화 (.isMinimized)
w.restore() # 화면 원복
w.close() # 윈도우 닫기, 저장여부도 물어봄

    ## 키보드 ##

w = pyautogui.getWindowsWithTitle("제목 없음")[0] 
w.activate() # 노트가 활성화되면서 클릭이 활성화. 활성이 안된다면 클릭코드를 넣어줘야겠지.
pyautogui.write("12345") 
pyautogui.write(["left","3","right","enter"],interval=0.25)
pyautogui.write("super_son", interval=0.25)

# shift 4 -> $ (특수문자)
pyautogui.keyDown("shift") # 쉬프트 키를 누른 상태에서
pyautogui.press("4") # 숫자 4를 입력하고 
pyautogui.keyUp("shift") # 쉬프트 키를 뗀다

# 간단하게 핫키를 이용
pyautogui.hotkey("ctrl", "shift", "a")
# 뜻은 1,2,3 차례대로 누르고 3,2,1 순으로 떼는것.

# 한글 처리(클립보드에 내용을 복붙하는 개념)
import pyperclip
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

    ## 메세지 박스 ##

pyautogui.alert("자동화 수행에 실패하였습니다.","경고") # 확인 버튼만 있는 팝업
result = pyautogui.confirm("계속 진행하시겠습니까?","확인") # 확인과 취소버튼이 있는 팝업
print(result) # OK와 Cancel이 있네 (이 값을 활용할수있겠지. 다른애들도 마찬가지)
pyautogui.prompt("파일명을 무엇으로 하시겠습니까?","입력") # 사용자 입력 팝업
pyautogui.password("암호를 입력하세요") # 암호 입력

    ## 로그 log ## (터미널과 파일에 함께 로그 남기는 법)

import logging
from datetime import datetime

# 시간 로그레벨 메시지 형태로 로그작성이엿지
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("log_test_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")

    ## 파일과 폴더 기본 ##

import os
import time
import datetime
 
print(os.getcwd()) # 현재 작업공간
os.chdir("2_DESKTOP") # 으로 작업 공간 이동
os.chdir("../..") # 부모의 부모폴더로 이동 ../../ 계속 상위로
file_path = os.path.join(os.getcwd(),"myfile.txt") # 절대 경로 생성

# 파일 생성 날짜 (수정일. 접근일. 크기등은 11번 파일에 있어)
file_path = "trash.png"
ctime = os.path.getctime(file_path)
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S")) 

# 파일 목록 하위 폴더 포함시켜서 가져오기
result = os.walk(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA") # 그냥 (".") 해도 현재 파이썬 작업공간을 불러온다 
for root, dirs, files in result:
    print(root, dirs, files) # 이 순서대로 보여줄 수도 있네.

# 파일 어디있는지, 있는지 없는지 찾아주는 코드
import fnmatch
pattern = "file*.png" # file로 시작하고 .py로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding") :
    for name in files :
        if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
            result.append(os.path.join(root,name))
print(result)

# 주어진 경로가 파일인지 폴더인지?
print(os.path.isdir("2_DESKTOP")) # 2_DESKTOP은 폴더인가? True
print(os.path.isfile("2_DESKTOP")) # 2_DESKTOP은 파일인가? False

# 만약에 지정된 경로에 해당하는 파일/폴더가 없다면?
os.chdir(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\베이스 공부") # 이렇게 작업공간을 바꿔주고
print(os.path.isfile("캡처1.png"))
print(os.path.isdir("2_DESKTOP")) 
 
    ## 파일과 폴더 작업 ##

open("new_file.txt","a").close() # 빈 파일 생성
os.rename("new_file.txt", "new_file_rename.txt") # 이름변경
os.remove("new_file_rename.txt") # 파일 삭제하기
os.mkdir(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA\1_EXCEL\new_folder") # 절대경로 기준으로 폴더생성
os.makedirs("Test_folder/a/b/c") # 하위폴더 가진 폴더 만들기(mkdir로 하면 실패)
os.rename("Test_folder","newname") # 폴더명 변경하기
os.rmdir("newname") # 폴더 안이 비어있을때만 삭제가능

import shutil
shutil.rmtree("newname") 
# 폴더 안이 비어있지않아도 완전 삭제가능(모든 파일이 삭제될 수 있으므로 주의!)!

# 파일 복사하기(어떤 파일을 폴더 안으로 복사하기)
shutil.copy("trash.png","test_folder") # 원본 경로, 대상 경로
shutil.copy("trash.png","test_folder/copied_trash.png") # 파일명까지 변경시켜서
shutil.copyfile("trash.png","test_folder/copied_trash2.png") # 이 코드는 폴더 쓸수 없고, 파일명만 쓸수 있다.
shutil.copy2("trash.png","test_folder/copy2.png") # 거의 똑같다고 보면되는데..
# copy, copyfile : 메타정보 복사 x (얘는 새로운 파일을 만든거)
# cop2 : 메타정보 복사 O (생성일자 까지 똑같고.. 완전 복제)

# 폴더 복사(파일 쓰면안되)
shutil.copytree("test_folder","test_folder2") # 원본 폴더 경로, 대상 폴더 경로 / 하위 내용까지 다 복사

# 폴더 이동
shutil.move("test_folder","test_folder3") # 앞 얘를 뒤 얘 밑으로 들어가게한다.
# 하나의 폴더명이 보이지않는다면 폴더명을 그것으로 바꾸는 역할을 하기도 한다.