# IMail? 인가 하는것도 있다는데 쓰기가 불편해서 다른걸로
# pip install imap-tools로 설치
from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com",993)
mailbox.login(Email_address, Email_password, initial_folder="INBOX") # 기본 수신함을 설정해놓는 과정. 다른걸로 하고싶다면 찾아서 하면되겠지

for msg in mailbox.fetch(limit=1, reverse=True): # 그냥 ()로 하면 모든 메일을 다 가져오는것이다.
    # limit : 개수를 한개, reverse : False 라면 옛날꺼부터 가져온다.
    print("제목", msg.subject)
    print("발신자", msg.from_)
    print("수신자", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date)
    print("본문", msg.text)
    # print("HTML 메시지", msg.html)
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

########## 여기서 gmt에 대한설명 #############
# msg,date 부분에 맨 뒷부분이 +3 , -3 이런식을 띄고 있는데 이것은 gmt에 해당한다
# 구글에 gmt-8이라 검색해보면 세계표준시간에 맞춰 - + 로 조정된 값인데 우린 gmt+9 이고
# 로스앤젤레스는 gmt-8이므로 그들의 시간에 17시간을 더하면 우리시간이 되는것이다.