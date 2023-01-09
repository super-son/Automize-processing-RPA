# pip install openpyxl
from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성 (이건 하나의 파일)
ws = wb.active # 현재 활성화된 sheet 가져옴 (위에서 만든 sheet 가져옴)
ws.title = "NadoSheet" # sheet의 이름을 변경

wb.save("sample.xlsx")
wb.close()