to_list = ["newhj1447@naver.com", "hj1447@hanmail.net","123"]
msg = ", ".join(to_list) # join에 대한 문법적인 부분도 알고가라
print(msg)
msg2 = ":".join(to_list)
print(msg2)

# 시간에 대해서 이런식의 형식들로 응용이 가능하다!
import time
print(time.strftime('%a-%b-%Y'))
import datetime
dt= datetime.datetime.strptime("2021-03-01","%Y-%m-%d")
print(dt.strftime('%d-%m-%a-%Y'))
