# 메일함을 열고 제목이 파이썬 특강 신청합니다. 를 찾고 닉네임과 전화번호를 꺼내와서 리스트로 저장하는것까지
from account import *
from imap_tools import MailBox

applicant_list = [] # 지원자 리스트

with MailBox("imap.gmail.com", 993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox:
    index = 1 # 순번을 위해
    for msg in mailbox.fetch('(SENTSINCE 01-MAR-2021)'): # 2020년 11월 7일 이후로 온 메일 조회
        if "파이썬 특강 신청" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번 : {} 닉네임 : {} 전화번호 : {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

for applicant in applicant_list:
    print(applicant)