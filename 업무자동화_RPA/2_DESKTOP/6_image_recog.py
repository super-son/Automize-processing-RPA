import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu) # 사진을 찾았네!! (찾는방식은 y=0부터해서 x축을 타고 쭉 훑고 y += 이런식의 원리)
pyautogui.click(file_menu) # 딱 중간부분을 클릭한다!
# window 아이콘 + shift + s 누르고 영역캡쳐! > 자동으로 클립보드 저장
# 그림판에 붙여넣은뒤 자르기로 필요없는 영역삭제

trash = pyautogui.locateOnScreen("trash.png")
pyautogui.moveTo(trash) # 이게 밑에 있다보니까 시간이 좀 걸리네 

vs_cap = pyautogui.locateOnScreen("vs_cap.png")
pyautogui.moveTo(vs_cap) # 해상도가 바뀌거나하면 못찾아. 그래서 작업환경과 똑같이 되어야되.

# https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox 참고
# 똑같은 체크박스가 여러개 있네
for i in pyautogui.locateAllOnScreen("check.png"):
    print(i)
    pyautogui.click(i, duration=0.25)
# AllOn이 아니라 그냥 On 이였으면 제일 위에꺼만 처음발견되서 체킹됨

######################################

trash = pyautogui.locateOnScreen("trash.png")
pyautogui.moveTo(trash) 
###################################
##### 이거 속도를 개선해보자 
####################################

# 1. GrayScale : 흑백으로만 이미지를 판별해서 30퍼 정도의 효율을 올린다
# trash = pyautogui.locateOnScreen("trash.png",grayscale=True)
# pyautogui.moveTo(trash) 

# 2. 범위 지정 : 말 그대로 찾는 범위를 지정해준다. region=(x,y,width,height)
# trash = pyautogui.locateOnScreen("trash.png",region=(1600, 450, 400, 250))
# pyautogui.moveTo(trash) 
# pyautogui.mouseInfo()로 파악해서 대략값을 잡아준다.
# 1806,566

# 3. 정확도 조정 : 픽셀 하나하나가 똑같진않아도 퍼센트이상 넘으면 같다고 간주한다
# pip install opencv-python
# trash = pyautogui.locateOnScreen("trash.png", confidence=0.9) # 90퍼센트의 일치확률. 자기가 적정선을 찾아야되.
# pyautogui.moveTo(trash) 

######################################
######################################

# 자동화 대상이 바로 보여지지 않는 경우 

# 1. 계속기다리기
note_file_menu = pyautogui.locateOnScreen("note_file_menu.png")
if note_file_menu: # 이건 답 X
    pyautogui.click(note_file_menu)
else:
    print("발견실패") # while 문을 쓰면되겠네!

while note_file_menu is None:
    note_file_menu = pyautogui.locateOnScreen("note_file_menu.png")
    print("발견 실패")

pyautogui.click(note_file_menu)
print("실행 완료")

# 2. 일정 시간동안 기다리기 (타임아웃)
import time 
import sys

timeout = 10 # 10초 대기
start = time.time()  # 시작 시간 설정(아 현재의 시간!)
note_file_menu = None # 정의되어있지않아서 변수를 할당 + True로하면 안되
while note_file_menu is None:
    note_file_menu = pyautogui.locateOnScreen("note_file_menu.png")
    end = time.time() # 종료 시간 설정 
    if end - start > timeout : # 지정한 10초를 초과한다면
        print("시간 종료")
        sys.exit()

##################################################### 함수를 만들어볼게 (ㅈㄴ 어렵누)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout :
            break
    pyautogui.moveTo(target)
    print(target) # 필요하면 return으로 바꿔


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found({img_file}). Terminate program.")
        sys.exit()

#########################################################################함수 사용해보자

# find_target("file_menu.png",10)
my_click("note_file_menu.png", 10)



