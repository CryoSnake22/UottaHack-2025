import os
import re
from urllib.parse import urlparse
from ada_url import parse_url
import time

# get all files in the files directory and print them nicely


rootpath = os.getcwd() + "\\"

fileDirectory = "files" + "\\"

toOperate = rootpath + fileDirectory +"sample.txt"
userPasswordPattern =r":[^:]+:[^:]+$"
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
        line2 = re.sub(userPasswordPattern,"",line)
        if line.__len__() > 0:
            try:
                username_password = re.search(userPasswordPattern, line)
                user = ""
                pas = ""
                if username_password:
                    user = username_password.group(0)[1:].split(':')[0]
                    pas = username_password.group(0)[1:].split(':')[1]
                    adaObj = parse_url(line2)
                    adaObj['username'] = user
                    adaObj['password'] = pas
                    adaObj['application'] = ''
                adaList.append(adaObj)
            except ValueError:
                errorList.append(line)
            linenum += 1

    print("{:.2f} seconds for ada_url".format(time.time() - start))
# print(errorList)
print(len(errorList))
with open(rootpath + "files/oddOnes.txt", encoding="utf-8", mode="w") as f:
    # Define regex patterns for domain, application, and port extraction
    domain_pattern = r'(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})'
    application_pattern = r'@([a-zA-Z0-9._-]+(?:\.[a-zA-Z0-9._-]+)+)\/'
    port_pattern = r':(\d{2,5})'

    # Prepare a list to collect parsed data
    parsed_data = []
    for item in errorList:
        # Process each entry
        domain_match = re.search(domain_pattern, item)
        application_match = re.search(application_pattern, item)
        port_match = re.search(port_pattern, item)
        username_password = re.search(userPasswordPattern, line)
        user = ""
        pas = ""
        if username_password:
            user = username_password.group(0)[1:].split(':')[0]
            pas = username_password.group(0)[1:-1].split(':')[1]

        parsed_data.append({
            "href": item.strip(),
            "host": domain_match.group(1) if domain_match else None,
            "hostname": domain_match.group(1) if domain_match else None,
            "application": application_match.group(1) if application_match else None,
            "port": port_match.group(1) if port_match else None,
            "username": user,
            "password": pas,
            "protocol": "",
            "pathname": "",
            "search": "",
            "hash": ""
            })
print(adaList[110:220])
print(parsed_data[110:120])