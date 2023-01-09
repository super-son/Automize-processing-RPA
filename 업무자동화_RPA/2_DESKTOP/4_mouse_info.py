import pyautogui
pyautogui.mouseInfo() # 현재 마우스의 좌표와 색상을 알려주는 툴! F1을 누르면 복사
# pyautogui.FAILSAFE = False # 이건 참고만해라.. 그냥 마우스 코드에서 이런 류의 에러가 나면 사용하는 코드
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep을 적용시키는 코드

for i in range(10):
    pyautogui.move(100,100)
    # pyautogui.sleep(1) #(pyautogui.PAUSE = 1) 위에 이 코드가 있어서 없어도 되지 