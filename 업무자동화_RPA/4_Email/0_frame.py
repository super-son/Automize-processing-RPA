# account.py 도 함께 봐야되!

    # 메일 보내기

import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = Email_address # 보내는 사람
msg["To"] = "newhj1447@naver.com" # 받는 사람
msg.set_content("본문입니다. 첨부파일이 있다면 그것을 다운로드 하세요") # 본문

# 여러 명에게 메일을 보낼 때
# msg["To"] = "newhj1447@naver.com, hj1447@hanmail.net" # 그냥 이렇게 해도 되고
to_list = ["newhj1447@naver.com", "hj1447@hanmail.net"]
msg["To"] = ", ".join(to_list)

# 첨부파일 보낼때
with open("check.png", "rb") as f: # 읽어오기 + 바이너리모드
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
# mine 타입에 관련된 글 : https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address,Email_password)
    smtp.send_message(msg)

###########################################################################################################################

    # 메일 받기

from imap_tools import MailBox
from account import *

## 베이스 ##

mailbox = MailBox("imap.gmail.com",993)
mailbox.login(Email_address, Email_password, initial_folder="INBOX") # 기본 수신함을 설정

for msg in mailbox.fetch(limit=1, reverse=True): # limit : 개수를 한개, reverse : False 라면 옛날꺼부터 가져온다.
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    print("날짜", msg.date)
    print("본문", msg.text)
    print("="*100)

    # 첨부 파일
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        # 파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))
            print("=======")

mailbox.logout()

## 응용 ##

# with 문으로 logout 코드를 안써도 된다.
with MailBox("imap.gmail.com",993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox : 
    
    # 1. 베이스
    for msg in mailbox.fetch(limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject)) # 최근 5개 메일 보낸사람, 제목가져오기

    # 2. 읽지않은
    for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 가져오기(쿼리를 이용하는것) / 똑같이 limit이나 reverse 등의 옵션을 줄 수 있다
        print("[{}] {}".format(msg.from_, msg.subject))

    # 3. 특정인
    for msg in mailbox.fetch('(FROM newhj1447@gmail.com)'): # 특정인의 메일 가져오기
        print("[{}] {}".format(msg.from_, msg.subject))

    # 4. 포함글자(제목, 본문)
    for msg in mailbox.fetch('(TEXT "paypal")'): # 어떤 글자를 포함하는 메일(제목, 본문)
        # "text mail" 이런식으로 띄었면 각각의 단어로 봐서 포함하는 메일을 찾게된다. or의 기능인거지
        print("[{}] {}".format(msg.from_, msg.subject))

    # 5. 포함글자(제목)
     for msg in mailbox.fetch('(SUBJECT "paypal")'): # 어떤 글자를 포함하는 메일(제목만). 
        print("[{}] {}".format(msg.from_, msg.subject))

    # 위 방법들의 조건부분에서 지금 한글지원은 어렵다..!
    # 그래서 대체 방법을 알려주겟어!
    for msg in mailbox.fetch(limit=5, reverse=True): # 그래서 가져온 다음 이렇게 if를 활용해서 걸러주는 방법이 있지!
        if "테스트" in msg.subject: # 이건 제목에 대한 코드지.
            print("[{}] {}".format(msg.from_, msg.subject))

    # 6. 날짜
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5): # 특정 날짜 이후의 메일
        print("[{}] {}".format(msg.from_, msg.subject))
    for msg in mailbox.fetch('(ON 17-Nov-2020)', reverse=True, limit=5): # 특정 날짜에 온 메일
        print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일(AND)
    for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020 SUBJECT "paypal")', reverse=True, limit=5): # 이런식으로 이어쓸 수 있다. and 조건!
        print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 중의 조건을 만족하는 메일(OR)
    for msg in mailbox.fetch('(OR SENTSINCE 07-Nov-2020 SUBJECT "paypal")', reverse=True, limit=5): # OR을 이렇게 앞에써준다.
        print("[{}] {}".format(msg.from_, msg.subject))
  
################################################################################################################ 

    # 활용편

# 이 형태를 잘 기억해라
# 이게 지금 나혼자 보내고 나혼자 받는 거라서 헷갈릴수도 있겠지만, 지금 과정은 내가 일단 보내고 내가 참가신청을 받는 과정.

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

################################################################################################################ 

# 참가신청된 메일들을 받는과정

from account import *
from imap_tools import MailBox
import smtplib
from email.message import EmailMessage
from openpyxl import Workbook

max_val = 3 # 최대 선정자 수
applicant_list = [] # 지원자 리스트

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox:
    index = 1 # 순번을 위해
    for msg in mailbox.fetch('(SENTSINCE 01-MAR-2021)'): # 2020년 11월 7일 이후로 온 메일 조회
        if "파이썬 특강 신청" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(Email_address,Email_password) 

    for applicant in applicant_list:
        to_addr = applicant[0].from_ # 수신 메일 주소(msg = applicant[0])
        # index = applicant[1]
        # nickname = applicant[2]
        # phone = applicant[3] 밑에랑 같은 뜻
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val :
            title = "파이썬 특강 안내 [선정]"
            content = "{}님 축하드립니다. 특강대상자로 선정되셨습니다. (선정순번 {}번)".format(nickname, index)
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (선정순번 {}번)".format(nickname, index - max_val)
        
        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = Email_address
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname, "님에게 메일 발송 완료")

print("[3. 선정자 명단 파일 생성]")
wb = Workbook()
ws = wb.active
ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_val]: # 0,1,2 (3위까지!)
    ws.append(applicant[1:]) #index, nickname, phone 이였지 아까 1,2,3이

wb.save("result.xlsx")

print("모든 작업이 완료되었습니다.")

    
         



