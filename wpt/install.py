from os import system, path
from wpt.download import download
from time import sleep
import requests

a = 'Do you want to install '
c = "? [Y/n]:"
h = ".exe"


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
