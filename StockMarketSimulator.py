import json
import time
from numpy import random
text = "/Users/Ben/Desktop/Coding/python/StockMarketSimulator.json"
def update():
    file = open(text)
    current = json.loads(file.readline())
    file.close()
    topop = ""
    
    file = open(text, 'w')
    for key in current["Stocks"]:
        cs = current["Stocks"]
        cs[key] += round(random.normal(loc=0, scale=0.05), 2)
        cs[key] = round(cs[key], 2)
        if cs[key] <= 0:
            cs[key] = 0
            topop = key
        current["Stocks"] = cs
    cs = current["Stocks"]
    ci = current["Indexes"]
    try:
        ci["$SEV"] = cs["LEMO"] + cs["BLDG"] + cs["GRCY"]
        ci["$SEV"] = round(ci["$SEV"], 2)
    except:
        print("'$SEV' needs to be updated.")
    try:
        ci["$TEK"] = cs["NETW"] + cs["MESG"] + cs["TELE"]
        ci["$TEK"] = round(ci["$TEK"], 2)
    except:
        print("'$TEK' needs to be updated.")
    current["Indexes"] = ci
    if topop != "":
        if topop in current["User"]["Stocks"]:
            current["User"]["Stocks"].pop(topop)
        current["Stocks"].pop(topop)
        topop = ""
    file.write(json.dumps(current))
    file.close()
    
for x in range(5):
    update()
request = raw_input("+> ")
while not "quit" in request.lower() and not "exit" in request.lower():
    for x in range(5):
        update()
    file = open(text)
    current = json.loads(file.readline())
    file.close()
    rf = request[:request.find(" ")]
    re = request[request.find(" ")+1:]
    cs = current["Stocks"]
    cu = current["User"]
    ci = current["Indexes"]
    if rf == "info":
        if re == "account":
            print(cu)
        elif re in cs:
            print(cs[re])
        elif re in ci:
            print(ci[re])
        else:
            print(cs,ci)
    if rf == "buy":
        rm = re[:re.find(" ")]
        re = int(re[re.find(" ")+1:])
        if rm in cs:
            if cs[rm] * re < cu["Cash"]:
                cu["Cash"] -= cs[rm] * re
                if not rm in cu["Stocks"]:
                    cu["Stocks"][rm] = {"quantity": re, "purchase": cs[rm], "current": cs[rm]}
                else:
                    cu["Stocks"][rm] += re
    accval = 0
    for stock in cu["Stocks"]:
        accval += cs[stock] * cu["Stocks"][stock]["quantity"]
        cu["Stocks"][stock]["current"] = cs[stock]
    cu["Total"] = round(accval + cu["Cash"], 2)
    cu["Cash"] = round(cu["Cash"], 2)
    current["User"] = cu
    file = open(text, 'w')
    file.write(json.dumps(current))
    file.close()
    request = raw_input("+> ")