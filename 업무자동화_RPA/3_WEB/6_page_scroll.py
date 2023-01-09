from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window() 
url = 'https://search.shopping.naver.com/search/all?query=%EB%A7%88%EC%9A%B0%EC%8A%A4&cat_id=&frm=NVSHATC'
browser.get(url)

import time
interval = 2 #2초에 한번씩 스크롤을 내릴꺼야

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이(얘는 계속 더해지네)를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        # 맨 밑 까지 온거니까
        break
    prev_height = curr_height #else 의 뜻
# 맨 위로 올려주기
browser.execute_script('window.scrollTo(0,0)')

print("~종료~")