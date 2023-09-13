from prompt_toolkit import prompt
from os import system
from download import download

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
