# coding:utf-8
'''
@ author:LingYing
@ 功能:Windows上的软件包管理器
'''

from os import system, path
from time import sleep
import requests
import click
import csv
import fnmatch
from tqdm import tqdm
import requests
import pandas as pd
from util import *

a = 'Do you want to install '
b = None
c = "? [Y/n]:"
h = ".exe"
lists = []

f = open(".\list.csv", "r")  # 打开list.csv
# with f:  # 在list.csv文件中
reader = csv.reader(f, delimiter=",")
header_row = next(reader)
urls, parameters, names, fss, uninstalls = [], [], [], [], []  # 创建列表用于读取数据
for row in reader:
    load_name = str(row[0])  # 读取name列
    load_url = str(row[1])  # 读取url列
    load_parameter = str(row[2])  # 读取parameter列
    load_uninstall = str(row[3])
    load_fs = (row[4])  # 读取fs列
    names.append(load_name)  # 将name添加到names列表中
    urls.append(load_url)  # 将url添加到urlss列表中
    parameters.append(load_parameter)  # 将parameter添加到parameters列表中
    uninstalls.append(load_uninstall)
    fss.append(load_fs)  # 将fs添加到fss列表中

installed = pd.read_csv("installed.csv")

# 计数
count = 0
line_count = len(names)  # 计算list.csv的行数
for i in range(line_count):  # 循环list.csv的行数次
    # 将urls, parameters, names, fss中的值赋给依次get_name, get_url, get_parameter, get_fs
    get_name = str(names[count])
    get_url = str(urls[count])
    get_parameter = str(parameters[count])
    get_uninstall = str(uninstalls[count])
    get_fs = int(fss[count])
# 计数加一
count += 1


@click.group(invoke_without_command=True)
# @click.argument("name")
@click.option("-i", "--install", help="install the program", nargs=1)
@click.option("-s", "--search", help="search the program", nargs=1)
@click.option("-g", "--getfilesize", help="get the size of the file", nargs=1)
@click.option("-r", "--remove", help="remove the program", nargs=1)
def main(install=None, search=None, remove=None, getfilesize=None):
    count = 0
    lists_count = 0
    for i in range(line_count):
        get_name = names[count]
        get_url = urls[count]
        get_parameter = parameters[count]
        get_uninstall = str(uninstalls[count])
        get_fs = fss[count]
    if install != None:
        if fnmatch.fnmatch(get_name, install) == True:
            anzhuang(get_name, get_url, get_parameter, get_url)
        else:
            print("没有找到:(")
    else:
        pass
    if search != None:
        count = 0
        for i in range(line_count):
            if fnmatch.fnmatch(names[count], '*'+search+'*') == True:
                lists.append(names[count])
                count += 1
            else:
                count += 1
        print(lists[lists_count])
        lists_count += 1
    if remove != None:
        count = 0
        judgment = remove in installed.values
        if judgment == True:
            index = names.index(remove)
            uninstall_software(uninstalls[index])
        else:
            print("没有找到:(")
    if getfilesize != None:
        count = 0
        for i in range(line_count):
            if fnmatch.fnmatch(names[count], '*'+getfilesize+'*') == True:
                download(urls[count], names[count]+h)
                fs = path.getsize(names[count]+h)
                system("del .\\"+names[count]+h)
                print(fs)
                break
            else:
                count += 1
    else:
        pass


count += 1
f.close()
installed.close()


def download(url: str, fname: str):
    resp = requests.get(url, stream=True)
    total = int(resp.headers.get('content-length', 0))
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


def anzhuang(name, url, parameter, fs):
    # 下载部分
    def dl():
        print("\033c", end="")
        print("Program Installer V2.0".center(120))
        print("下载中...")
        download(url, name+h)

    # 错误处理部分
    def error():
        print("\033c", end="")
        print("Program Installer V2.0".center(120))
        print("检查一下网络再试吧")
        sleep(2)

    print("\033c", end="")
    print("Program Installer V2.0".center(120))
    get = input("是否要安装"+name+c)  # 获取用户输入
    # 确认要安装
    if get == "Y" or get == "y" or get == '':
        try:
            judgment = path.isfile(name+h)  # 判断是否已经存在要下载的文件
            fsize = path.getsize(name+h)  # 判断文件大小是否正确(单位:字节)
        except FileNotFoundError:
            pass
            # 不存在或大小不正确
            if judgment == False or fsize != int("get_fs"):
                try:
                    dl()  # 进行下载
                    b = True  # 记录是否下载正确的文件
                except requests.exceptions.ConnectionError:  # 没有连接网络时的错误处理
                    error()  # 进行错误处理
                    b = False  # 记录是否下载正确的文件
            # 存在或大小正确
            elif judgment == True or fsize == int("get_fs"):
                b = True  # 记录是否下载正确的文件
        # 已经下载正确的文件,进行安装
        if b == True:
            print("\033c", end="")
            print("Program Installer V2.0".center(120))
            print("安装中...")
            sleep(2)
            system(name+h+parameter)  # 安装
            system("del "+name+h)  # 删除文件
            print("\033c", end="")
            print("Program Installer V2.0".center(120))
            print("安装完毕")
            sleep(2)
        # 没有下载正确的文件,跳过
        else:
            print("\033c", end="")
            print("Program Installer V2.0".center(120))
            print("安装失败")
            sleep(1)
    # 不进行安装,跳过
    elif get == "N" or get == "n":
        pass
    # 用户输入不正确,提示用户进行正确的输入
    else:
        print("\033c", end="")
        print('请输入"Y"或"N"')
        sleep(1)


if __name__ == '__main__':
    main()

# 结束安装
print("\033c", end="")
system("CLS")
print("Program Installer V1.8".center(120))
print("三秒后退出")
sleep(3)
system("CLS")
print("\033c", end="")
