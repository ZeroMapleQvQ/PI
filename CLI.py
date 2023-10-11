# coding:utf-8
"""
@ author:LingYing
@ 功能:Windows上的软件包管理器
"""

from os import system, path
from time import sleep
import click
import csv
from fnmatch import fnmatch
from tqdm import tqdm
# from pandas import *
from uninstall.util import *
from wpt.install import install_
from wpt.download import download

judgment = None
h = ".exe"
search_lists = []


# programs_lists = read_csv("csvs\list.csv")
# installed_list = read_csv(".\csvs\installed.csv")  # .to_dict()
# line_count = len(programs_lists)  # 计算list.csv的行数
# programs_lists.to_dict()
# programs_lists = DataFrame(programs_lists)
# installed_list.to_dict()
# installed_list = DataFrame(installed_list)

# name_list = list(programs_lists.name)
# url_list = list(programs_lists.url)
# parameter_list = list(programs_lists.parameter)
# uninstall_list = list(programs_lists.uninstall)
# filesize_list = list(programs_lists.filesize)
# installed_list = list(installed_list.name)
# output_list = []

f = open(".\csvs\list.csv", "r")  # 打开list.csv
reader = csv.reader(f, delimiter=",")
header_row = next(reader)
urls, parameters, name_list, filesizes, uninstalls = [], [], [], [], []  # 创建列表用于读取数据
for row in reader:
    load_name = str(row[0])  # 读取name列
    load_url = str(row[1])  # 读取url列
    load_parameter = str(row[2])  # 读取parameter列
    load_uninstall = str(row[3])
    load_fs = (row[4])  # 读取fs列
    name_list.append(load_name)  # 将name添加到name_list列表中
    urls.append(load_url)  # 将url添加到urls列表中
    parameters.append(load_parameter)  # 将parameter添加到parameters列表中
    uninstalls.append(load_uninstall)
    filesizes.append(load_fs)  # 将fs添加到fss列表中
dict = {"name": name_list, "url": urls, "parameter": parameters,
        "uninstall": uninstalls, "filesize": filesizes}


"""
# 计数
count = 0
for i in range(line_count):  # 循环list.csv的行数次
    # 将urls, parameters, name_list, fss中的值赋给依次get_name, get_url, get_parameter, get_fs
    get_name = str(name_list[count])
    get_url = str(urls[count])
    get_parameter = str(parameters[count])
    get_uninstall = str(uninstalls[count])
    get_fs = int(filesizes[count])
# 计数加一
count += 1
"""


@click.group(invoke_without_command=True)
@click.option("-i", "--install", help="install the program", nargs=1)
@click.option("-s", "--search", help="search the program", nargs=1)
@click.option("-g", "--getfilesize", help="get the size of the file", nargs=1)
@click.option("-r", "--remove", help="remove the program", nargs=1)
def main(install=None, search=None, remove=None, getfilesize=None):
    count = 0
    lists_count = 0
    """
    for i in range(line_count):
        get_name = name_list[count]
        get_url = urls[count]
        get_parameter = parameters[count]
        get_uninstall = str(uninstalls[count])
        get_fs = filesizes[count]
    """
    if install != None:
        judgment = install in programs_lists.values
        if judgment == True:
            index = name_list.index(install)
            if fnmatch(name_list[index], install) == True:
                install_(name_list[index], url_list[index],
                         parameter_list[index], filesize_list[index])
        else:
            print("没有找到:(")
    else:
        pass
    if search != None:
        count = 0
        for i in range(line_count):
            if fnmatch(name_list[count], '*'+search+'*') == True:
                search_lists.append(name_list[count])
                count += 1
            else:
                count += 1
    if len(search_lists) == 0:
        print("没有找到:(")
    else:
        print(search_lists)
    if remove != None:
        count = 0
        # index1 = installed_list[installed_list["name"] == remove]
        # index2 = installed_list[installed_list["name"] == remove.index.tolist()[
        # 0]]
        # judgment = fnmatch(installed_list[count], remove)
        # judgment = remove in installed_list.values
        try:
            uninstall_software(
                installed_list.loc.name[installed_list[installed_list["name"] == remove.index.tolist()[0]]])
        except:
            print("没有找到:(")
    if getfilesize != None:
        count = 0
        for i in range(line_count):
            if fnmatch(name_list[count], '*'+getfilesize+'*') == True:
                download(url_list[count], name_list[count]+h)
                fs = path.getsize(name_list[count]+h)
                system("del .\\"+name_list[count]+h)
                print(fs)
                break
            else:
                count += 1
    else:
        pass


# count += 1
# f.close()


if __name__ == '__main__':
    print(dict)
    main()
