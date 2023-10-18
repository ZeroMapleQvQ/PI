from os import system, path
from time import sleep
import sqlite3
import click
import csv
from fnmatch import fnmatch
from tqdm import tqdm
import numpy
# from pandas import *
from uninstall.util import *
from wpt.install import install_
from wpt.download import download

judgment = None
h = ".exe"
search_lists = []

file_path = "csvs/list.csv"

def loaddb():
    global db
    global cur
    db = sqlite3.connect("list.db")
    cur = db.cursor()

def closedb():
    try:
        db.commit()
        cur.close()
        db.close()
    except:
        pass

@click.group(invoke_without_command=True)
@click.option("-i", "--install", help="install the program", nargs=1)
# @click.argument("install", nargs=-1)
@click.option("-s", "--search", help="search the program", nargs=1)
@click.option("-g", "--getfilesize", help="get the size of the file", nargs=1)
@click.option("-r", "--remove", help="remove the program", nargs=1)
def main(install=None, search=None, remove=None, getfilesize=None):
    loaddb()
    if install != None:
        cur.execute("SELECT name FROM scores")
        results_names = cur.fetchall()
        cur.execute("SELECT * FROM scores")
        results_all = cur.fetchall()
        print(results_names)
        print(results_all[0])
        for i in range(0, len(results_names)):
            try:
                storage = results_names
                del(results_names)
                results_names = []
                results_names.append(storage[i][0])
                print(results_names)
                print(install)
            except:
                pass
            if install in results_names:
                    print(install[0])
                    print(install)
                    install_(results_all[i][0], results_all[i][1], results_all[i][2], results_all[i][3])
            else:
                print("没有找到:(")
        db.commit()
        cur.close()
        db.close()
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
    closedb()

if __name__ == '__main__':
    main()
