import requests
import hashlib

from server import consts

eth_list_url = "https://etherscan.io/accounts/{}?ps=100"


headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


def get_eth_richlist():
    out = ""
    for x in range(1, 2):
        r = requests.get(eth_list_url, headers=headers)
        # for x in r.text.split("<tr"):

        # print(str(r.text).split("<tr>")[3].split("<td>")[2:5])
        lines = str(r.text).split("<tr>")[2:101]
        for line in lines:
            items = line.split("<td>")[2:5]
            addr = items[0].split("address/")[1][:42]
            balance = "".join(items[2][:10].split(','))
            salted_addr = addr + consts.salt
            hashed_addr = hashlib.sha256(salted_addr.encode())
            out += '"' + hashed_addr.hexdigest() + '"'
            out += ','
    return out


richlist = get_eth_richlist()
with open("richlist.py", "w") as f:
    f.write("richlist = [" + richlist[:-1] + "]")
