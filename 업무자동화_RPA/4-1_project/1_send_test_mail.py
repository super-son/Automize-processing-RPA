# 이게 지금 나혼자 보내고 나혼자 받는 거라서 헷갈릴수도 있겠지만, 지금 과정은 내가 일단 보내고 내가 참가신청을 받는 과정.

# 신청 메일 양식
# 제목 : 파이썬 특강 신청합니다
# 본문 : 닉네임/전화번호 뒤 4자리 (랜덤)
# 예 : 나도코딩/1234

import smtplib
from random import *
from account import *
from email.message import EmailMessage

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address,Email_password)
    
    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다"
        msg["From"] = Email_address
        msg["To"] = "newhj1447@gmail.com"

        # content = nickname + "/" + str(randint(1000,9999))
        content = "/".join([nickname, str(randint(1000,9999))])
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 메일 발송 완료")
         