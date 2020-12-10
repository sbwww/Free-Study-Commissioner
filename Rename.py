import os
import re
import sys

import StuList

CHN_NUMBER = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']

PREFIX = ""
SUFFIX = "实验"

input_suffix = input("实验几：")
if input_suffix.isdigit():
    SUFFIX += CHN_NUMBER[(int)(input_suffix)]
else:
    SUFFIX += input_suffix

SUFFIX += "."

input_course = input("什么课：")
# 按照课程增加和修改 elif
if input_course[0] == 'w' or input_course[0] == 'W':
    SLIST = StuList.WEB_LIST
    filelist = os.listdir("web实验")
    currentpath = os.getcwd()
    os.chdir(r"web实验")
elif input_course[0] == 'c' or input_course[0] == 'C':
    SLIST = StuList.CSHARP_LIST
    filelist = os.listdir("c#实验")
    currentpath = os.getcwd()
    os.chdir(r"c#实验")


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
print("Expected:   " + str(expected) + "\t files.")
print("Received:   " + str(received) + "\t files.")
print(" Renamed:   " + str(renamed) + "\t files.")
for student in SLIST:
    if str(student[0]) not in received_list:
        print(str(student[0])+"\t"+str(student[1])+"\tnot received!")

os.chdir(currentpath)
sys.stdin.flush()

os.system("pause")
