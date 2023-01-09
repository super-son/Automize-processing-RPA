# 활용예시 : 휴대폰 제각기 이름이 다른 사진들을 일괄적으로 이름변경후 폴더 관리할 때

# 파일 기본
import os
# print(os.getcwd()) # 현재 작업공간
# os.chdir("2_DESKTOP") # 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동 ../../ 계속 상위로
# print(os.getcwd())
# os.chdir("c:/")  # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(),"myfile.txt") # 절대 경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime
 
# # 파일의 생성 날짜
# file_path = "trash.png"
# ctime = os.path.getctime(file_path)
# print(ctime)
# # 날짜정보를 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime))
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime))

# # 파일 크기
# size = os.path.getsize(file_path)
# print(size) # 바이트 단위로 파일 크기 가져오기 

# 파일 목록 가져오기
# print(os.listdir()) # 현재 작업공간의 모든 폴더, 파일 목록 가져오기
# print(os.listdir("2_DESKTOP")) # 주어진 폴더에서 ...

# 파일 목록 하위 폴더 포함시켜서 가져오기
# result = os.walk(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA") # 그냥 (".") 해도 현재 파이썬 작업공간을 불러온다 
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files) # 이 순서대로 있는 거 다 보여주지

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()): # ("."을 썼어도 같은 뜻이지만 join시 .은 root가 .이라고만 되서 절대경로를 못만드네)
#     # [a.txt, b.txt,11_file_system.py,..]
#     if name in files:
#         result.append(os.path.join(root, name)) # 이렇게 합쳐줘서 절대경로로 만드는 것
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = "file*.png" # file로 시작하고 .py로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk(".") :
#     for name in files :
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치하면
#             result.append(os.path.join(root,name))
# print(result)

# # 주어진 경로가 파일인지 폴더인지?
# print(os.path.isdir("2_DESKTOP")) # 2_DESKTOP은 폴더인가? True
# print(os.path.isfile("2_DESKTOP")) # 2_DESKTOP은 파일인가? False

# print(os.path.isdir("check.png")) # false
# print(os.path.isfile("check.png")) # true

# # 만약에 지정된 경로에 해당하는 파일/폴더가 없다면?
# print(os.path.isfile("checking.png")) # false

# 주어진 경로가 존재하는지?
# if os.path.exists("2_DESKTOP"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않아요")

# 파일 만들기(간단한 버전)
# open("new_file.txt","a").close() # 빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt") # 이름변경

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# # os.mkdir("new_folder") # 작업공간에 만들어줌
# os.mkdir(r"C:\Users\hj144\Desktop\손휘준의 개인폴더\Coding\Python\업무자동화_RPA\1_EXCEL\new_folder") # 절대경로 기준으로 폴더생성

# 하위 폴더를 가지는 폴더 만들기
# os.makedirs("Test_folder/a/b/c") # mkdir로 하면 실패한다

# 폴더명 변경하기
# os.rename("Test_folder","newname")

# 폴더 지우기
# os.rmdir("newname") # 폴더 안이 비어있을때만 삭제가능

import shutil
# shutil.rmtree("newname") # 폴더 안이 비어있지않아도 완전 삭제가능(하위 폴더있어도 ㅇㅇ)
# # 모든 파일이 삭제될 수 있으므로 주의!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("trash.png","test_folder") # 원본 경로, 대상 경로
# shutil.copy("trash.png","test_folder/copied_trash.png") # 파일명까지 변경시켜서
# shutil.copyfile("trash.png","test_folder/copied_trash2.png") # 이 코드는 폴더 쓸수 없고, 파일명만 쓸수 있다.
# shutil.copy2("trash.png","test_folder/copy2.png") # 거의 똑같다고 보면되는데..

# copy, copyfile : 메타정보 복사 x (얘는 새로운 파일을 만든거)
# cop2 : 메타정보 복사 O (생성일자 까지 똑같고.. 완전 복제)

# 폴더 복사(파일 쓰면안되)
# shutil.copytree("test_folder","test_folder2") # 원본 폴더 경로, 대상 폴더 경로 / 하위 내용까지 다 복사

# 폴더 이동
# shutil.move("test_folder","test_folder3") # 앞 얘를 뒤 얘 밑으로 들어가게한다.
# 하나의 폴더명이 보이지않는다면 폴더명을 그것으로 바꾸는 역할을 하기도 한다.
# 
#  




