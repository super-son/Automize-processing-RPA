from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options # 새로 배운거

# 다운로드 위치를 정해준다
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA'})

# 옵션으로 추가해주고 ㅇㅋㅇ 다운로드하니까 지정한 경로로 다운이되네
browser = webdriver.Chrome(options=chrome_options)
url = 'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download'
browser.get(url)
time.sleep(2)


# download 링크 클릭

browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('/html/body/p[2]/a/img')
elem.click()


time.sleep(5)
browser.quit()