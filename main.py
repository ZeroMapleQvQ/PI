<<<<<<< HEAD
import csv
from install import install
from prompt_toolkit import prompt
from os import system
from tqdm import tqdm
import requests
from download import download

'''
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
'''

'''
a="Do you want to install "
c="? [Y/n]:"
g="%APPDATA%\\ProgramInstaller\\Cache\\"
h=".exe"
def install(name,url,parameter):
    print("\033c", end = "")
    get = prompt(a+name+c)
    if get == "y" or get == "":
        print("Downloading...")
        download(url,name+h)
        print("Installing...")
        system(name+h+parameter)
        system("del "+name+h)
        print("Done")
        print("\033c", end = "")
    elif get == "n":
        print("\033c", end = "")
    else:
        print("Please enter 'y' or 'n'")
    # input("Press 'Enter' to exit")
'''

f = open(".\list.csv","r")
with f:
    #reader = csv.DictReader(f,delimiter=",")
    #list = [*csv.DictReader(f,delimiter=",")]
    reader = csv.reader(f,delimiter=",")
    header_row = next(reader)
    urls,parameters,names = [],[],[]
    for row in reader:
        name = str(row[0])
        url = str(row[1])
        parameter = str(row[2])
        names.append(name)
        urls.append(url)
        parameters.append(parameter)
    #print(names)
    # print(urls)
    # print(parameters)

name_count = 0
url_count = 0
parameter_count = 0
count = len(names)

for i in range(count):
    name1 = str(names[name_count])
    url1 = str(urls[url_count])
    parameter1 = str(parameters[parameter_count])
    install(name1,url1,parameter1)
    name_count += 1
    url_count += 1
    parameter_count += 1
=======
import csv
from install import install
from prompt_toolkit import prompt
from os import system
from tqdm import tqdm
import requests
from download import download

'''
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
'''

'''
a="Do you want to install "
c="? [Y/n]:"
g="%APPDATA%\\ProgramInstaller\\Cache\\"
h=".exe"
def install(name,url,parameter):
    print("\033c", end = "")
    get = prompt(a+name+c)
    if get == "y" or get == "":
        print("Downloading...")
        download(url,name+h)
        print("Installing...")
        system(name+h+parameter)
        system("del "+name+h)
        print("Done")
        print("\033c", end = "")
    elif get == "n":
        print("\033c", end = "")
    else:
        print("Please enter 'y' or 'n'")
    # input("Press 'Enter' to exit")
'''

f = open(".\list.csv","r")
with f:
    #reader = csv.DictReader(f,delimiter=",")
    #list = [*csv.DictReader(f,delimiter=",")]
    reader = csv.reader(f,delimiter=",")
    header_row = next(reader)
    urls,parameters,names = [],[],[]
    for row in reader:
        name = str(row[0])
        url = str(row[1])
        parameter = str(row[2])
        names.append(name)
        urls.append(url)
        parameters.append(parameter)
    #print(names)
    # print(urls)
    # print(parameters)

name_count = 0
url_count = 0
parameter_count = 0
count = len(names)

for i in range(count):
    name1 = str(names[name_count])
    url1 = str(urls[url_count])
    parameter1 = str(parameters[parameter_count])
    install(name1,url1,parameter1)
    name_count += 1
    url_count += 1
    parameter_count += 1
>>>>>>> 836d3115c835a327feedf42f5004d8fbd636f4aa
