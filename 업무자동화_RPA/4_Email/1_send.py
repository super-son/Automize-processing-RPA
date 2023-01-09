# account.py 먼저 보고오도록.. 1_account.py 저장하니까 import를 못하네 1_ 때메..
import smtplib
from account import *

# 기본적인 방법
# http://pythonstudy.xyz/python/article/508-%EB%A9%94%EC%9D%BC-%EB%B3%B4%EB%82%B4%EA%B8%B0-SMTP : 참고자료
# with 문은 보통 close를 명시해주지 않아 생기는 에러를 막기위해 한 블록당 시작과 끝을 처리해주는 코드라는데.. 그런걸로..
with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # port 번호 587
    smtp.ehlo() # 연결이 잘 수립되는지 확인. smtp 서버에 인사보내는거
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(Email_address, Email_password) # import한 변수들을 이용해 로그인

    subject = "test mail" # 메일 제목
    body = "mail body" # 메일 본문

    msg = f"Subject: {subject}\n{body}" # 약속된 형태
    smtp.sendmail(Email_address, "newhj1447@naver.com", msg) # 발신자, 수신자. 정해진 형식의 메시지
