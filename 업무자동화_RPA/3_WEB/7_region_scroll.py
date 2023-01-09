from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window() 
url = 'https://www.w3schools.com/html/'
browser.get(url)
time.sleep(1)
# 보니까 페이지 로딩이 다 될때까지 계속 기다렷다가 1초 후 실행되네..
# 자 그리고 이건 만약에 스크롤 내리든 안내리든 원래 업데이트 되어있는 상태라면 굳이 안해도 되는 동작들이야.

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[76]') # 지역의 제일 밑에있는 항목의 xpath를 딴거
# 방법 1 : ActionChain
# from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2:
xy = elem.location_once_scrolled_into_view # 함수가 아니라서 ()쓰면 안되
print("type : ", type(xy))
print("value : ", xy)
elem.click()

time.sleep(1)
browser.quit()