from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com",993)
# mailbox.login(Email_address, Email_password, initial_folder="INBOX") # 이걸쓰면 logout까지 써줘야 하기때문에 with문으로 더 짧게 보여줌
# mailbox.logout()

with MailBox("imap.gmail.com",993).login(Email_address, Email_password, initial_folder="INBOX") as mailbox : 
    
    # 쓸 수 있는 조건들은 이 외에도 많으니까 찾아보도록
    # 1. 베이스
    for msg in mailbox.fetch(limit=5, reverse=True):
        print("[{}] {}".format(msg.from_, msg.subject)) # 최근 5개 메일 제목가져오기

    # 2. 읽지않은
    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 가져오기(쿼리를 이용하는것) / 똑같이 limit이나 reverse 등의 옵션을 줄 수 있다
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 3. 특정인
    # for msg in mailbox.fetch('(FROM newhj1447@gmail.com)'): # 특정인의 메일 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 4. 포함글자(제목, 본문)
    # 작은 따옴표로 먼저 감싸고, 실제 TEXT 부분은 큰 따옴표로 감싸주세요. 바껴도 되는데, 안헷갈려야지
    # for msg in mailbox.fetch('(TEXT "paypal")'): # 어떤 글자를 포함하는 메일(제목, 본문)
    #     # "text mail" 이런식으로 띄었면 각각의 단어로 봐서 포함하는 메일을 찾게된다. or의 기능인거지
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 5. 포함글자(제목)
    #  for msg in mailbox.fetch('(SUBJECT "paypal")'): # 어떤 글자를 포함하는 메일(제목만). 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 위 방법들의 조건부분에서 지금 한글지원은 어렵다..!
    # 그래서 대체 방법을 알려주겟어!
    # for msg in mailbox.fetch(limit=5, reverse=True): # 그래서 가져온 다음 이렇게 if를 활용해서 걸러주는 방법이 있지!
    #     if "테스트" in msg.subject: # 이건 제목에 대한 코드지.
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 6. 날짜
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse=True, limit=5): # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    # for msg in mailbox.fetch('(ON 17-Nov-2020)', reverse=True, limit=5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 2가지 이상의 조건을 모두 만족하는 메일(AND)
    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020 SUBJECT "paypal")', reverse=True, limit=5): # 이런식으로 이어쓸 수 있다. and 조건!
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # # 2가지 중의 조건을 만족하는 메일(OR)
    # for msg in mailbox.fetch('(OR SENTSINCE 07-Nov-2020 SUBJECT "paypal")', reverse=True, limit=5): # OR을 이렇게 앞에써준다.
    #     print("[{}] {}".format(msg.from_, msg.subject))
  

