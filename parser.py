import os
from urllib.parse import urlparse
import time

#get all files in the files directory and print them nicely


rootpath = os.getcwd() + "\\"

fileDirectory = "files" + "\\"

toOperate = rootpath + fileDirectory +"sample.txt"
resultList = []


with open(toOperate, encoding="utf-8", errors="ignore") as f:
    start = time.time()
    linenum = 1
    for line in f:
        if line.__len__() > 0:
            resultList.append(str(urlparse(line)))

print("{:.2f} seconds".format(time.time() - start))

