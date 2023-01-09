from selenium import webdriver
from selenium.webdriver.common.by import By # 10번 줄에 필요한거!
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')
browser.switch_to.frame('iframeResult')
# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]') 
elem = browser.find_element(By.XPATH,'//*[@id="vehicle1"]') # 이거 그냥 윗줄이랑 똑같은 뜻인데 다른방식알랴줌.

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()
else:
    print("선택 되어 있으므로 아무것도 안함")

time.sleep(5)

browser.quit()