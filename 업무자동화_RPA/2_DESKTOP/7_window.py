import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창(vscode)
# print(fw.title) # 창의 제목 정보
# print(fw.size) # 창의 크기정보(width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보. 자동 꼭짓점
# pyautogui.click(fw.left + 25 , fw.top + 20)

# for w in pyautogui.getAllWindows():
#     print(w) # 모든 윈도우 가져오기

# for w in pyautogui.getWindowsWithTitle("제목 없음"): # 켜져있고 + 저장이 안된 메모장과 그림판이 있다면 그들을 리스트로 가져오네
#     print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
# print(w)

if w.isActive == False : # 현재 활성화가 되지 않았다면, 이라는 뜻인데 실험결과 있든없든 실행되는데...
    w.activate() # 활성화 시키기 (맨 앞으로 가져오기, 내린창 말고.. 뒤에 숨은 창 적용!)

if w.isMaximized == False : # 얘는 힘이 좋네 ㅋㅋ. 숨어있어도 걍 끄집어 내는데
    w.maximize() # 최대화

# if w.isMinimized == False :
#     w.minimize() # 최소화

pyautogui.sleep(2)
w.restore() # 화면 원복
w.close() # 윈도우 닫기. 만약 내용이 있다면 저장할지 자동으로 물어보네.