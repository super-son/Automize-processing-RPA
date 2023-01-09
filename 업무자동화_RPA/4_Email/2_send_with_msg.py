import smtplib
from account import *
from email.message import EmailMessage

# 앞의 정해진 형식보단 훨씬 가독성이 있고 한글사용도 가능해!

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = Email_address # 보내는 사람
msg["To"] = "newhj1447@naver.com" # 받는 사람

# 여러 명에게 메일을 보낼 때
# msg["To"] = "newhj1447@naver.com, hj1447@hanmail.net" # 그냥 이렇게 해도 되고
to_list = ["newhj1447@naver.com", "hj1447@hanmail.net"]
msg["To"] = ", ".join(to_list) # join에 대한 문법적인 부분도 알고가라

# # 참조 (뭐.. 그런게 있나봐)
# msg["Cc"] = "newhj1447@naver.com"
# # 비밀참조
# msg["Bcc"] = "newhj1447@naver.com"

msg.set_content("테스트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address,Email_password)
    smtp.send_message(msg)


