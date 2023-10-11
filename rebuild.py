from os import system, path
from time import sleep
import sqlite3
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

file_path = "csvs/list.csv"
# f = open(file_path, "r")
# csv_reader = csv.reader(f)
# csv_writer = csv.writer(f)

db = sqlite3.connect("list.db")
cur = db.cursor()

cur.execute("SELECT name FROM scores WHERE name == 'Everything'")
db.commit()
if cur.fetchall() == "Everything":
    db.commit()
    print("True")
z = cur.fetchall(cur.execute(
    "SELECT name FROM scores WHERE name == 'Everything'"))
print(z)
# print(db)

db.commit()
cur.close()
db.close()

# z = "INSERT INTO scores VALUES('Everything', 'https://www.voidtools.com/Everything-1.4.1.1024.x64-Setup.exe', '/S', 1, 'Everything 1.4.1.1024 (x64)', 'Flase')"
# cur.execute(z)


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
        pass
    if search != None:
        pass
    if remove != None:
        with open(file_path, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if remove in row[0]:
                    print(row[0])
                    column4_value = row[4]
                    row[5] = "False"
                    uninstall_software(column4_value)
                    # csv_reader.close()
                    csv_writer = csv.writer(f)
                    csv_writer.writerow()
    if getfilesize != None:
        pass


if __name__ == '__main__':
    main()
