from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option_selected')
browser.switch_to.frame('iframeResult')

# cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 옵션을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')
# elem.click()
# option[1] : 1번째 항목
# option[2] : 2번째 항목
# ...
time.sleep(3)

# 완전일치하는 텍스트 값을 통해 선택하는 방법 [옵션 중에서 텍스트가 Audi인 항목을 선택하는거지]
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Volvo"]') # 위의 xpath값을 보고 내가 직접 적은값.
# elem.click()

# 부분일치하는 텍스트 갓을 통해 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Vol")]') 
elem.click()

time.sleep(3)
browser.quit()



