from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # iframe의 id 코드를 복붙 > frame 전환
elem = browser.find_element_by_xpath('//*[@id="male"]')

time.sleep(5) # 5초 대기

### 선택이 안되어 있으면 선택하기 !!!
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("선택 되어 있으므로 아무것도 안함")



