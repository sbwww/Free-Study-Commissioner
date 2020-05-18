import os
import re
import sys

from StuList import *

PREFIX = "计科(5)班"
SUFFIX = "实验六."

filelist = os.listdir("实验6")
currentpath = os.getcwd()
os.chdir(r"实验6")

expected = len(SLIST)
received = len(filelist)
renamed = 0
received_list = []
# 改名
for filename in filelist:
    split_name = filename.split('-')
    if len(split_name) == 1:
        sNo = filename[6:18] if filename[6:18].isdigit() else filename[6:17]
        received_list.append(sNo)
        continue
    if len(split_name) != 3:
        print(filename+" \t ERROR!")
        continue
    sNo = split_name[0]  # 学号
    sName = split_name[1]  # 姓名
    docType = split_name[2].split('.')[1]  # 文件类型
    os.rename(filename, PREFIX+sNo+sName+SUFFIX+docType)
    received_list.append(sNo)
    renamed += 1

# print(received_list)
print("Expected: " + str(expected) + "\t files.")
print("Received: " + str(received) + "\t files.")
print(" Renamed: " + str(renamed) + "\t files.")
for student in SLIST:
    if str(student[0]) not in received_list:
        print(str(student[0])+" "+str(student[1])+" not received!")

os.chdir(currentpath)
sys.stdin.flush()
