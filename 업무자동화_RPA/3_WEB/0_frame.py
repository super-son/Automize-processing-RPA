from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() 
url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio'
browser.get(url)

######################################################################################### 웹 상의 다운로드 경로 지정하기

from selenium.webdriver.chrome.options import Options 
# 다운로드 위치를 정해준다
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA'})
# 옵션으로 추가해주고 ㅇㅋㅇ 다운로드하니까 지정한 경로로 다운이되네
browser = webdriver.Chrome(options=chrome_options) # 그러니까 얘들이 상단부에 적혀있어야 할 코드들이지

#########################################################################################

# framge 전환 : body안에서 새로운 html문서형식을 띄는 것에 대하여 코딩할때
browser.switch_to.frame('iframeResult') # iframe의 id 코드를 복붙 > frame 전환

elem = browser.find_element_by_xpath('//*[@id="male"]')
elem.click()

# iframe에서 상위로 빠져 나옴
browser.switch_to_default_content()

#########################################################################################

    ### 라디오 버튼, 체크박스 선택 ###

# '선택이 안되어 있으면 선택하기' 코드 !!!
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있다면
    print("선택 되어 있으므로 아무것도 안함")

    ### 콤보박스(리스트) 선택 ###

# xpath를 따보면 [elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')] 인데 숫자만 조정해서 .click으로 해도되지만!

# 완전일치하는 텍스트 값을 통해 선택하는 방법 [옵션 중에서 텍스트가 Audi인 항목을 선택하는거지]
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Volvo"]') # 위의 xpath값을 보고 내가 직접 적은값.
elem.click()

# 부분일치하는 텍스트 갓을 통해 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(),"Vol")]') 
elem.click()

######################################################################## 

# 똑같은 표현임
elem = browser.find_element_by_xpath('//*[@id="vehicle1"]') 
from selenium.webdriver.common.by import By
elem = browser.find_element(By.XPATH,'//*[@id="vehicle1"]')
# 끄적끄적
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

################################################################################## xpath의 극한의 효율
# 실제로 작업할때는 몇 번째의 순번을 띠는 xpath는 언제든지 변할수 있기 때문에 text 값으로 처리하는것이 낫다.
# 그런데 또 그냥 text로 하기에는 코드 내 중복되는 text가 나올 수도 있으므로 xpath와 text를 모두 이용하는 방식이 가장 좋다.
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click() 이것을
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 이렇게 해주면
# a 하위까지 범위를 좁힌 후 text값이 contact form 인것을 찾는것이다!!
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 이건 포함단어를 찾는것인데
# 텍스트도 2020, 2021 처럼 변하는 값이라면 이렇게 포함값을 해주면 좋지!
###################################################################################

    ### 스크롤 내리기 ###

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

    ### 페이지 일부의 스크롤 ###

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[76]') # 지역의 제일 밑에있는 항목의 xpath를 딴거
# 방법 1 : ActionChain
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법 2 : 좌표이용
xy = elem.location_once_scrolled_into_view # 함수가 아니라서 ()쓰면 안되
print("type : ", type(xy))
print("value : ", xy)
elem.click()

##################################################################### 자세한건 9번파일 ㄱㄱ

curr_handle = browser.current_window_handle # 현재 윈도우 핸들 정보 저장

# 다른 브라우저넘어가는 버튼 클릭
browser.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[2]/a').click()

# 브라우저 이동
handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    browser.switch_to.window(handle) # 각 핸들로 이동해서
    print(browser.title) # 출력해보면 현재 핸들 (브라우저)의 제목 표시
    print()

# 그 브라우저를 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to_window(curr_handle)

#####################################################################

browser.quit()