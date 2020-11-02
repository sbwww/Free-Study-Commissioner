import os
import re
import sys

import StuList

PREFIX = ""
SUFFIX = "实验一."
SLIST = StuList.WEB_LIST

filelist = os.listdir("web实验")
currentpath = os.getcwd()
os.chdir(r"web实验")

expected = len(SLIST)
received = len(filelist)
renamed = 0
received_list = []
startPos = len(PREFIX)
endPos = startPos+12

# 改名
for filename in filelist:
    split_name = filename.split('-')
    if len(split_name) == 1:
        if filename[startPos:endPos].isdigit():
            sNo = filename[startPos:endPos]
        else:
            SNo = filename[startPos:endPos-1]
        received_list.append(sNo)
        continue
    if len(split_name) != 2:
        print(filename+" \t ERROR!")
        continue
    sNo = split_name[0]  # 学号
    sName = split_name[1].split('.')[0]  # 姓名
    docType = split_name[1].split('.')[1]  # 文件类型
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
