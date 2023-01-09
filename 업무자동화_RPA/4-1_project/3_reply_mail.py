# 합격자와 불합격자에게 답장해준다. 선착순 3명만 당첨.
from account import *
from imap_tools import MailBox

import smtplib
from email.message import EmailMessage

max_val = 3 # 최대 선정자 수
applicant_list = [] # 지원자 리스트

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox:
    index = 1 # 순번을 위해
    for msg in mailbox.fetch('(SENTSINCE 01-MAR-2021)'): # 2020년 11월 7일 이후로 온 메일 조회
        if "파이썬 특강" in msg.subject:
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
        to_addr = applicant[0].from_ # 수신 메일 주소
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