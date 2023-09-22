import csv
from install import install
from download import download
from time import sleep

f = open(".\list.csv", "r")  # 打开list.csv
with f:  # 在list.csv文件中
    reader = csv.reader(f, delimiter=",")
    header_row = next(reader)
    urls, parameters, names, fss = [], [], [], []  # 创建列表用于读取数据
    for row in reader:
        name = str(row[0])  # 读取name列
        url = str(row[1])  # 读取url列
        parameter = str(row[2])  # 读取parameter列
        fs = (row[3])  # 读取fs列
        names.append(name)  # 将name添加到names列表中
        urls.append(url)  # 将url添加到urlss列表中
        parameters.append(parameter)  # 将parameter添加到parameters列表中
        fss.append(fs)  # 将fs添加到fss列表中

# 计数
count = 0
line_count = len(names)  # 计算list.csv的行数


for i in range(line_count):  # 循环list.csv的行数次
    # 将urls, parameters, names, fss中的值赋给依次get_name, get_url, get_parameter, get_fs
    get_name = str(names[count])
    get_url = str(urls[count])
    get_parameter = str(parameters[count])
    get_fs = int(fss[count])
    # 以get_name, get_url, get_parameter, get_fs作为参数进行安装
    # install(get_name, get_url, get_parameter, get_fs)
    # 计数加一
    count += 1
# 结束安装
print("\033c", end="")
print("Program Installer V1.8".center(120))
print("三秒后退出")
sleep(3)
