# <html>
#     <body>
#         <iframe id="1">
#             <html>
#                 <body>..
                
#         <iframe id="2">
#             <html>
#                 <body>..
#     </body>
# </html> 의 형태를 띄기때문에.. 접근성에 있어서 독립적이다.
# 만약 웹에서 저런 형태를 띈다면 iframe 밑 버튼에 대해 xpath를 따서 접근한다면 찾지못할것이다.
# 그래서 그냥하면안되고 frame 전환을 해줘야 한다.
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # iframe의 id 코드를 복붙 > frame 전환

elem = browser.find_element_by_xpath('//*[@id="male"]')
elem.click()

browser.switch_to_default_content() # iframe에서 상위로 빠져 나옴

browser.quit()