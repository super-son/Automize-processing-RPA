# 작업물이 어떤 식으로 진행되었는지 로그를 남기는 것
import logging

logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s [%(levelname)s] %(message)s") # 디버그 레벨이상 모든 로그를 다 찍어준다는 의미
# 시간정보, 로그레벨정보, 로그정보 순서
# .debug가 아니라 .error 였다면 밑에 애들 중에 2개만 떳겠지.

# # 지금 예시로 나열된 순서가 로그레벨 낮은순서 - > 높은순서
# logging.debug("아 이거 누가 짠거야~") # 개발단계에서 쓰는거
# logging.info("자동화 수행 준비") # 배포했을때부터는 레벨을 올려서 사용자들에게도 보이게.
# logging.warning("이 스크립트는 조금 오래 되었습니다. 실행상에 문제가 있을 수 있습니다.")
# logging.error("에러가 발생하였습니다. 에러 코드는...")
# logging.critical("복구가 불가능한 심각한 문제가 발생했습니다...")

# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime

# 시간 로그레벨 메시지 형태로 로그작성이엿지
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") 
logger = logging.getLogger()

# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log") # mylogfile_2020 10 21 14 10 11.log
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")

