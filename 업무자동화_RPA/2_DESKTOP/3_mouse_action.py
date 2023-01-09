import pyautogui
pyautogui.sleep(3) # 3초대기
print(pyautogui.position())

########################### 클릭을 해보자 ######################## 그림판 켜놓고 연습도 되네!!! 
pyautogui.click(64,17,duration=1) # 1초동안 (64,17) 좌표로 이동 후 마우스 클릭

pyautogui.click() # 이것은 

pyautogui.mouseDown() # 이둘을 합한것과 같은데
pyautogui.mouseUp() # 파일 드래그 앤 드랍을 할때 사용할 수 있다.

pyautogui.doubleClick() # 더블클릭
pyautogui.click(clicks=500) # 클릭 반복작업 횟수

pyautogui.rightClick() # 우클릭
pyautogui.middleClick() # 휠클릭

print(pyautogui.position()) # 으로 원하는 위치의 좌표확인! 먼저 한 후에
pyautogui.moveTo(976,38,duration=0.25)
pyautogui.drag(100,0,duration=0.25) # 현재 위치 기준으로 x는 100만큼, y는 0만큼 드래그!. 얘도 상대적이야
# drag에 duration 안 주면 시간이 너무 빨라서 drag를 못한다.
# 이 외에도 다른 것들도 실행이 안된다면 시간때문일수있다. 
pyautogui.dragTo(100,100,duration=0.25) # 얘는 절대성

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤.
# (-300) 이라면 아래 방향으로 스크롤.