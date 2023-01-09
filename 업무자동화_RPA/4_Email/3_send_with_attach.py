import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = Email_address # 보내는 사람
msg["To"] = "newhj1447@naver.com" # 받는 사람
msg.set_content("다운로드 하세요") # 본문

################################################################

# msg.add_attachment()
with open("check.png", "rb") as f: # 읽어오기 + 바이너리모드
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
# mine 타입에 관련된 글 : https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 보면된다.
# 여기서 매칭을 확인하고 알맞게 써주면 된다.
# 글 내용중에 application/octet-stream는 다른 모든 경우를 위한 기본값이라 설명되있어서. 잘 안 찾아지는건 이걸로 쓰면되겠지. 엑셀도 가능
# pdf 파일도 같이 첨부해볼게
with open("테스트용 파일.pdf", "rb") as f: # 읽어오기 + 바이너리모드
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

################################################################

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address,Email_password)
    smtp.send_message(msg)
