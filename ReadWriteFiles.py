# Reading and writing files in python
# Using shell utilities in python script using
# os module
# Using module zipfile


import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    f = open("textfile.txt", "a")
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")
    f.close()

    f = open("textfile.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)
    f.close()

    # OS path
    print(os.name)
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        path.getmtime("textfile.txt")
    )
    print("It has been " + str(td) + " since the file was modified")
    print(" Or, " + str(td.total_seconds()) + " seconds")

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dst = src + ".bak"
        shutil.copy(src, dst)
        shutil.copystat(src, dst)

        #os.rename("textfile.txt", "newfile.txt")
        #root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()