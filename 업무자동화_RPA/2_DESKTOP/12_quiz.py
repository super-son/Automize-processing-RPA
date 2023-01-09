import pyautogui
import pyperclip
import sys

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

pyautogui.keyDown("win") 
pyautogui.press("r") 
pyautogui.keyUp("win")

pyautogui.write("mspaint", interval=0.1) 
pyautogui.press("enter") 
pyautogui.sleep(2)

fw = pyautogui.getActiveWindow()
# fw = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]으로 해도 되지!
fw.maximize()

# 글자 버튼 클릭하는 코드 2가지
# pyautogui.click(398,92,duration=1)
btn_text = pyautogui.locateOnScreen("quiz_text.png") 
if btn_text:
    pyautogui.click(btn_text)
else:
    print("찾기 실패")
    sys.exit() # fw.close

# 흰 영역 클릭하는 코드 2가지
# pyautogui.click(495,417,duration=1)
btn_rotate = pyautogui.locateOnScreen("quiz_rotate.png")
pyautogui.click(btn_rotate.left+100 , btn_rotate.top+300) # (x좌표, y좌표)
# 이 방법은 찾으려는것보다 가변성이 적인 항목을 찾아 상대위치로 좌표를 구하는 방법이다.
# 개인 컴퓨터 설정마다 다른 부분들이 있기떄문에 절대적인 지표를 찾아 이렇게 활용할수 있다.

my_write("참 잘했어요")
pyautogui.sleep(5)

fw.close()
pyautogui.click(979,526,duration=1)


