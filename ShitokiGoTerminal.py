#version 2.1.1
# coding: utf-8

Encrypt = {
'a' : '00000',
'b' : '00010',
'c' : '00020',
'd' : '00100',
'e' : '00110',
'f' : '00120',
'g' : '00200',
'h' : '00210',
'i' : '00220',
'j' : '01000',
'k' : '01010',
'l' : '01020',
'm' : '01100',
'n' : '01110',
'o' : '01120',
'p' : '01200',
'q' : '01210',
'r' : '01220',
's' : '02000',
't' : '02010',
'u' : '02020',
'v' : '02100',
'w' : '02110',
'x' : '02120',
'y' : '02200',
'z' : '02210',
'A' : '10000',
'B' : '10010',
'C' : '10020',
'D' : '10100',
'E' : '10110',
'F' : '10120',
'G' : '10200',
'H' : '10210',
'I' : '10220',
'J' : '11000',
'K' : '11010',
'L' : '11020',
'M' : '11100',
'N' : '11110',
'O' : '11120',
'P' : '11200',
'Q' : '11210',
'R' : '11220',
'S' : '12000',
'T' : '12010',
'U' : '12020',
'V' : '12100',
'W' : '12110',
'X' : '12120',
'Y' : '12200',
'Z' : '12210',
'1' : '20000',
'2' : '20010',
'3' : '20020',
'4' : '20100',
'5' : '20110',
'6' : '20120',
'7' : '20200',
'8' : '20210',
'9' : '20220',
'0' : '21000',
'.' : '21010',
',' : '21020',
'>' : '21100',
'<' : '21110',
'/' : '21120',
'?' : '21200',
'\'' : '21210',
'"' : '21220',
':' : '22000',
';' : '22010',
'!' : '22020',
'@' : '22100',
'#' : '22110',
'$' : '22120',
'%' : '22200',
'^' : '22210',
'(' : '22220',
')' : '00001',
'{' : '00011',
'}' : '00021',
'[' : '00101',
']' : '00111',
'\\' : '00121',
'|' : '00201',
'+' : '00211',
'=' : '00221',
'-' : '01001',
'_' : '01011',
'`' : '01021',
'~' : '01101',
' ' : '01111'
}
def FW(value):
    encryption = ''
    for char in value:
        encryption = encryption + Encrypt[char]
    return encryption
        
def Decode(str):
    decode = ''
    arr = []
    for i in range(0,len(str),5):
         arr.append(str[slice(i,i+5,1)])
    for item in arr:
        for key, value in Encrypt.items():
            if value == item:
                    decode += key
    return decode
    
print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 
import webbrowser
import getpass
import datetime
os.system("say Hello, and welcome to the Shitoki Go! interactive terminal SGIT!")
usrpswd = {"Ben" : "brainlakeadmin1","Devin" : "brainlakeadmin2", }
usrshrt = {"Ben" : "ben", "Devin": "dvn",}
ysia = raw_input("Brainlake Username: ")
qqq = "0"
Qqq = "0"
if not ysia in usrpswd:
    qqq = "2"
else:
    usrshrtd = usrshrt[ysia]
pswd = getpass.getpass("Brainlake Password: ")
if qqq == "2" :
    print("I'm sorry, that is an invalid user account.")
elif pswd == usrpswd[ysia]:
    Qqq = "1"
    qqq = "1"

def search(query, number):       
    if number == "00" :
        if query[:8] == ".action." :
            if query[8:11] == "do." :
                action = query[11:]
                webbrowser.open("https://www.youtube.com/results?search_query=" + action)
            if query[8:14] == "speak." :
                saY = query[14:]
                os.system("say " + saY)
            if query[8:12] == "see." :
                sEeEeEE = query[12:]
                webbrowser.open("https://www.google.com/search?q=" + sEeEeEE  + "&sxsrf=ACYBGNQX_tF_V19Wx0-RCp1ahN-1bcB37A:1571603918943&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiHucPq2KvlAhWELn0KHVw2BZAQ_AUIEygC&biw=1440&bih=789")
            if query[8:12] == "run." :
                RuN = query[12:]
                os.system(RuN)
            if query[8:13] == "file." :
                queryF = raw_input("A4>>> ")
                qurye = query[13:]
                if qurye == "create":
                    os.system("cd /Users/Ben/Desktop/Coding/python ; touch " + queryF)
                if qurye == "erase":
                    password = getpass.getpass("Pswd>>> ")
                    if password == "securebrainlakeadmin":
                        file = open("/Users/Ben/Desktop/Coding/python/" + queryF, 'w')
                        file.close()
                if qurye == "read":
                    file = open("/Users/Ben/Desktop/Coding/python/" + queryF, 'r')
                    for line in file.readlines():
                        print(Decode(line))
                    file.close()
                if qurye == "append" :
                    file = open("/Users/Ben/Desktop/Coding/python/" + queryF, 'a')
                    queryW = raw_input("bgn>>> ")
                    file.write(FW(queryW))
                    file.close()
            if query[8:16] == "message.":
                if query[16:] == "create":
                    tojoin = raw_input("A4>>> ")
                    os.system("cd /Users/Ben/Desktop/Coding/python ; touch " + tojoin + "_message.txt")
                elif query[16:] == "seeall":
                    tojoin = raw_input("A4>>> ")
                    file = open("/Users/Ben/Desktop/Coding/python/" + tojoin + "_message.txt", 'r')
                    for line in file.readlines():
                        print(Decode(line))
                    file.close()
                else:
                    while True:
                        file = open("/Users/Ben/Desktop/Coding/python/" + query[16:] + "_message.txt",'r')
                        tong = 0
                        for line in file.readlines():
                            tong += 1
                            print(Decode(line))
                        file.close()
                        if tong == 0:
                            print("\\Nothing to see here!")
                        TEXt = raw_input("bgn>>> ")
                        if TEXt == ".quit":
                            break
                        else:
                            cu = datetime.datetime.now()
                            file = open("/Users/Ben/Desktop/Coding/python/" + query[16:] + "_message.txt",'a')
                            file.write(FW("[" + cu.strftime("%a") + ", " + cu.strftime("%d") + " " + cu.strftime("%b") + " " + cu.strftime("%Y") + " " + cu.strftime("%H") + ":" + cu.strftime("%M") + ":" + cu.strftime("%S") + "] usr_" + usrshrtd + " said " + TEXt) + "\n")
                            file.close()
            if query[8:10] == "SG":
                os.system("open '/Users/ben/Desktop/Coding/AppleScript/ShitokiGo.app'")
            if query[8:14] == "clock.":
                cu = datetime.datetime.now()
                if query[14:] == "time":
                    print(cu.strftime("%I") + ":" + cu.strftime("%M") + ":" + cu.strftime("%S") + " " + cu.strftime("%p")) 
                if query[14:] == "date":
                    print(cu.strftime("%A") + ", " + cu.strftime("%B") + " " + cu.strftime("%d") + ", " + cu.strftime("%Y")) 
                if query[14:] == "full":
                    print(cu.strftime("%I") + ":" + cu.strftime("%M") + ":" + cu.strftime("%S") + " " + cu.strftime("%p") + ", " + cu.strftime("%A") + ", " + cu.strftime("%B") + " " + cu.strftime("%d") + ", " + cu.strftime("%Y")) 
                if query[14:] == "terminal":
                    print(cu.strftime("%a") + ", " + cu.strftime("%d") + " " + cu.strftime("%b") + " " + cu.strftime("%Y") + " " + cu.strftime("%H") + ":" + cu.strftime("%M") + ":" + cu.strftime("%S"))
            if query[8:15] == "python.":
                os.system("python /Users/Ben/Desktop/Coding/python/" + query[15:])
            if query[8:13] == "wiki.":
                webbrowser.open("https://www.wikipedia.com/wiki/" + query[13:])
                
        if query[:5] == ".get.":
            qeri = query[7:]
            if query[5:7] == "A.":
                a = raw_input(qeri)
            if query[5:7] == "B.":
                b = raw_input(qeri)
            if query[5:7] == "C.":
                c = raw_input(qeri)
            if query[5:7] == "D.":
                d = raw_input(qeri)
            if query[5:7] == "E.":
                e = raw_input(qeri)
            if query[5:7] == "F.":
                f = raw_input(qeri)
            if query[5:7] == "G.":
                g = raw_input(qeri)
            if query[5:7] == "H.":
                h = raw_input(qeri)
            
            
if Qqq == "1" :
    while usrpswd[ysia] == pswd:
        query = raw_input("usr_" + usrshrtd + ">>> ")
        search(query, "00")
        if query == ".quit" :
            break
            
if qqq == "0":
    print("Oops, that's not the right password!")
    
#    '.action' is how you start everything.
#    '.action.file' deals with files.
#   '.action.do', '.action.see', and '.action.SGB' are all searches.
#   '.action.root.quit' to quit!