import os
import re
from urllib.parse import urlparse
from ada_url import parse_url
import time

#get all files in the files directory and print them nicely


rootpath = os.getcwd() + "\\"

fileDirectory = "files" + "\\"

toOperate = rootpath + fileDirectory +"sample.txt"
resultList = []
adaList = []
errorList = []

print(parse_url("https://cst-proxy-02.isqft.com8080"))
with open(toOperate, encoding="utf-8", errors="ignore") as f:
    start = time.time()
    linenum = 1
    # for line in f:
    #     if line.__len__() > 0:
    #         resultList.append(str(urlparse(line)))
    # print("{:.2f} seconds for urllib".format(time.time() - start))

    start = time.time()
    for line in f:
        line2 = re.sub(r":[^:]+:[^:]+$","",line)
        if line.__len__() > 0:
            try:
                adaList.append(parse_url(line2))
            except ValueError:
                errorList.append(line)
            linenum += 1

    print("{:.2f} seconds for ada_url".format(time.time() - start))
# print(errorList)
print(len(errorList))
with open(rootpath + "files/oddOnes.txt", encoding="utf-8", mode="w") as f:
    for item in errorList:
        f.write("%s" % item)
