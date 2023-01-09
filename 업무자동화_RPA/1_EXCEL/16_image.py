from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("image.png")
# C3 위치에 img 이미지 삽입
ws.add_image(img, "C3")

wb.save("sample_imgae.xlsx")
# pip install Pillow가 되어있어야 해!
# 이미지 불러오고 하는 작업에는 pillow가 있어야하는듯
# from PIL import ImageGrab
# from PIL import Image 이런식으로 사용하네