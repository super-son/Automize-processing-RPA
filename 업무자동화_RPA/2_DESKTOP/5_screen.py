import pyautogui
# 스크린 샷 찍기
pyautogui.sleep(3)
img = pyautogui.screenshot()
img.save("shotimage.png") # 파일로 저장

# pyautogui.mouseInfo()
# 29,17 63,170,242 #3FAAF2 (f1로 저장한 것)(29,17은 좌표 뒤 세개는 rgb값)

# pixel = pyautogui.pixel(29,17)
# print(pixel) # 이렇게 rgb값을 출력시킬수도 있다!

# print(pyautogui.pixelMatchesColor(29,17,pixel)) # 좌표값과 rgb값이 일치하는지 true or false 출력문
# print(pyautogui.pixelMatchesColor(29,17,(63,170,242))) # 같은 뜻


