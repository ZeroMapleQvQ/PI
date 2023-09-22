import csv
from install import install
from download import download
from time import sleep
from os import *

h = ".exe"

f = open('.\\list.csv', 'r')  # 打开list.csv
with f:  # 在list.csv文件中
    reader = csv.reader(f, delimiter=",")
    header_row = next(reader)
    urls, names = [], []  # 创建数组用于读取数据
    for row in reader:
        name = str(row[0])  # 读取name列
        url = str(row[1])  # 读取url列
        names.append(name)  # 将name添加到names数组中
        urls.append(url)  # 将url添加到urlss数组中

# 计数
name_count = 0
url_count = 0
count = len(names)  # 计算list.csv的行数

for i in range(count):  # 循环list.csv的行数次
    # 将urls,  names中的值依次赋给get_name, get_url
    get_name = str(names[name_count])
    get_url = str(urls[url_count])
    download(get_url,get_name+h)
    fs = path.getsize(name+h)
    # 计数加一
    name_count += 1
    url_count += 1
    print(fs)
input("6")