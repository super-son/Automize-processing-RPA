from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window() 
url = 'https://www.w3schools.com'
browser.get(url)

browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]').click()
# time.sleep(2)
browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()
# time.sleep(2)
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact Form")]').click()
# time.sleep(2)
################################################################################## xpath의 극한의 효율
# # 실제로 작업할때는 저렇게 몇 번째의 순번을 띠는 xpath는 언제든지 변할수 있기 때문에 text 값으로 처리하는것이 낫다.
# # 그런데 또 그냥 text로 하기에는 코드 내 중복되는 text가 나올 수도 있으므로 xpath와 text를 모두 이용하는 방식이 가장 좋다.
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click() 이것을
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click() # 이렇게 해주면
# # a 하위까지 범위를 좁힌 후 text값이 contact form 인것을 찾는것이다!!
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click() # 이건 포함단어를 찾는것인데
# # 텍스트도 2020, 2021 처럼 변하는 값이라면 이렇게 포함값을 해주면 좋지!
###################################################################################
First_Name = "나도"
Last_Name = "코딩"
Country = "Canada"
Subject = "퀴즈 완료하였습니다"

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(First_Name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(Last_Name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{0}"]'.format(Country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(Subject)

time.sleep(2)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
time.sleep(2)
browser.quit()