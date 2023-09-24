# coding:utf-8
'''
@ author:LingYing
@ 功能:Windows上的软件包管理器
'''

from os import system, path
from time import sleep
import click
import csv
from fnmatch import fnmatch
from tqdm import tqdm
from pandas import read_csv
from uninstall.util import *
from wpt.install import anzhuang
from wpt.download import download

b = None
c = "? [Y/n]:"
h = ".exe"
lists = []

f = open(".\csvs\list.csv", "r")  # 打开list.csv
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

installed = read_csv(".\csvs\installed.csv")

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
        if fnmatch(get_name, install) == True:
            anzhuang(get_name, get_url, get_parameter, get_url)
        else:
            print("没有找到:(")
    else:
        pass
    if search != None:
        count = 0
        for i in range(line_count):
            if fnmatch(names[count], '*'+search+'*') == True:
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
            if fnmatch(names[count], '*'+getfilesize+'*') == True:
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


if __name__ == '__main__':
    main()
