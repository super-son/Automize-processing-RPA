import pyautogui 

# 마우스 이동 [절대좌표]
pyautogui.moveTo(100,100) # (x,y) 지정한 위치로 마우스를 이동. 모니터 크기와 해상도에따라 다를수 있으니 주의!
pyautogui.moveTo(100,200, duration=0.25) # 0.25 초 동안 지정위치로 이동
pyautogui.moveTo(100,100)

# 마우스 이동 [상대좌표] - 현재 커서가 있는 위치로 부터
pyautogui.moveTo(100,200, duration=0.25)
print(pyautogui.position()) # 마우스 위치확인해주는 코드
pyautogui.move(100,100, duration=0.25) # (100,200) 기준으로 +100, +100 이동하는것이지
print(pyautogui.position())

# 얘도 마우스 위치확인해주는 코드!
p = pyautogui.position()
print(p[0], p[1]) # x,y
print(p.x, p.y) # x,y. 위에랑 같은거