import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate() # 불러오니까 자동으로 글자입력칸이 반짝거리네

# pyautogui.write("12345") # 만약 커서 활성화가 되어있지않으면 앞에 클릭코드를 넣어줘야겠지
# pyautogui.write("super_son", interval=0.25) # 글자마다 0.25초 간격
# pyautogui.write("나도코딩") # 한글은 안적힘 ㅎㅎ. pyautogui 는 영문과 숫자만 지원. 나중에 하는 법 설명

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# test 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 한번, la 치고 엔터누른다는 뜻

# 특수 문자 
# shift 4 -> $
# pyautogui.keyDown("shift") # 쉬프트 키를 누른 상태에서
# pyautogui.press("4") # 숫자 4를 입력하고
# pyautogui.keyUp("shift") # 쉬프트 키를 뗀다

# 조합키 (hot key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # 이 한줄과 같은거지. pyautogui.press("a")
# pyautogui.keyUp("ctrl") # ctrl + a : 전체선택 단축키

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", " shift", "a")
# ctrl 누르고 alt 누르고 shift 누르고 a 누르고 a 떼고 shift 떼고 alt 떼고 ctrl 뗀다
# pyautogui.hotkey("ctrl","a")

# 한글 처리
# pip install pyperclip
# 클립보드에 내용을 복붙하는 개념.. 지리네
import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나도코딩")

# 자동화 프로그램 사용 중 종료시키고 싶다. 당황하지말고
# win : ctrl + alt + del
# mac : cmd + shift + option + q
