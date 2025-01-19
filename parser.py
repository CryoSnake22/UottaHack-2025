import re
from ada_url import parse_url
import time
import sql_updater
import aiohttp
import asyncio
from concurrent.futures import ThreadPoolExecutor


# get all files in the files directory and print them nicely


# rootpath = os.getcwd() + "\\"
#
# fileDirectory = "files" + "\\"
#
# toOperate = rootpath + fileDirectory + "sample.txt"
#
async def fetch_status(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            return url, response.status
    except Exception as e:
        return url, f"Error: {e}"


async def fetch_all_statuses(urls):
    """
    Fetches the HTTP status codes for all URLs concurrently.
    :param urls: List of URLs to check.
    :return: List of tuples (URL, status_code or error message).
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        return await asyncio.gather(*tasks)


def parse_data():
    toOperate = "./files/sample.txt"
    userPasswordPattern = r":[^:]+:[^:]+$"
    resultList = []
    adaList = []
    errorList = []

    print(parse_url("https://cst-proxy-02.isqft.com8080"))
    start = time.time()
    with open(toOperate, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line2 = re.sub(userPasswordPattern, "", line)
            if line.__len__() > 0:
                try:
                    username_password = re.search(userPasswordPattern, line)
                    user = ""
                    pas = ""
                    if username_password:
                        user = username_password.group(0)[1:].split(":")[0]
                        pas = username_password.group(0)[1:].split(":")[1]
                        adaObj = parse_url(line2)
                        adaObj["username"] = user
                        adaObj["password"] = pas
                        adaObj["application"] = ""
                    adaList.append(adaObj)
                except ValueError:
                    errorList.append(line)

    # print(errorList)
    print(len(errorList))
    # with open(rootpath + "files/oddOnes.txt", encoding="utf-8", mode="w") as f:
    # Define regex patterns for domain, application, and port extraction
    domain_pattern = r"(?:https?:\/\/)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})"
    application_pattern = r"@([a-zA-Z0-9._-]+(?:\.[a-zA-Z0-9._-]+)+)\/"
    port_pattern = r":(\d{2,5})"

    # Prepare a list to collect parsed data
    parsed_data = []
    for item in errorList:
        # Process each entry
        domain_match = re.search(domain_pattern, item)
        application_match = re.search(application_pattern, item)
        port_match = re.search(port_pattern, item)
        username_password = re.search(userPasswordPattern, item)
        user = ""
        pas = ""
        if username_password:
            user = username_password.group(0)[1:].split(":")[0]
            pas = username_password.group(0)[1:-1].split(":")[1]

        parsed_data.append(
            {
                "href": item.strip(),
                "host": domain_match.group(1) if domain_match else None,
                "hostname": domain_match.group(1) if domain_match else None,
                "application": application_match.group(1)
                if application_match
                else None,
                "port": port_match.group(1) if port_match else None,
                "username": user,
                "password": pas,
                "protocol": "",
                "pathname": "",
                "search": "",
                "hash": "",
            }
        )
    combined_data = adaList + parsed_data
    urls = [
        entry["href"] for entry in combined_data if "href" in entry and entry["href"]
    ]

    # Fetch status codes asynchronously
    print(f"Fetching status codes for {len(urls)} URLs...")
    status_codes = asyncio.run(fetch_all_statuses(urls))

    # Map status codes back to the combined data
    status_code_map = {url: status for url, status in status_codes}
    for entry in combined_data:
        entry["status_code"] = status_code_map.get(entry["href"], None)

    print(f"{len(urls)} URLs processed in {time.time() - start:.2f} seconds.")
    print(combined_data[1])
    return combined_data
    print("{:.2f} seconds for ada_url".format(time.time() - start))
    print(adaList[1])
    return adaList + parsed_data


db_config = {
    "host": "localhost",
    "username": "root",
    "password": "root",
    "database": "deepcode",
}
table_name = "parsed_urls"

# data = [
#     {
#         "href": "https://user:pass@example.org:80/api?q=1#2",
#         "username": "user",
#         "password": "pass",
#         "protocol": "https:",
#         "host": "example.org:80",
#         "port": "80",
#         "hostname": "example.org",
#         "pathname": "/api",
#         "search": "?q=1",
#         "hash": "#2",
#     }
# ]


sql_updater.insert_data_in_batches(parse_data(), db_config, table_name)
# parse_data()
