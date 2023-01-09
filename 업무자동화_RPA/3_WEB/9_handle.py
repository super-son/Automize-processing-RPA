# 자동화에서 새 페이지를 여는 버튼을 클릭했을때, 두페이지 모두 컨트롤해야겠지.
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window() 
url = 'https://www.w3schools.com/tags/att_option_selected.asp'
browser.get(url)
## handle 이란걸 쓸거야
curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보

# 넘어가는 버튼 클릭
browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[2]/a').click()

# 브라우저 이동
handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle) # 각 핸들 정보
    browser.switch_to.window(handle) # 각 핸들로 이동해서
    print(browser.title) # 출력해보면 현재 핸들 (브라우저)의 제목 표시
    print()

# browser.find_element_by_xpath('//*[@id="framesize"]/span')
# browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/h1')

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to_window(curr_handle)

print(browser.title)

# 브라우저 컨트롤이 가능한지 확인
time.sleep(3)
browser.get('http://www.daum.net')

time.sleep(1)
browser.quit()