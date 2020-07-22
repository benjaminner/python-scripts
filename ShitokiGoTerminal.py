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
    for i in range(0,len(str),5):
         arr.append(str[slice(i,i+5,1)])
    for item in arr:
        for key, value in Encrypt.items():
            if value == item:
                    decode = decode + key
    return decode
    
print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 
import webbrowser
import getpass
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
    print("Oops, an unexpected error occured! Please tell Ben M. about this error so he can try to fix it!")
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
                    os.system("cd Desktop/Coding/python ; touch " + queryF)
                if qurye == "erase":
                    password = getpass.getpass("Pswd>>> ")
                    if password == "securebrainlakeadmin":
                        tst = open("Desktop/Coding/python/" + queryF, 'w')
                        tst.close()
                if qurye == "read":
                    file = open("Desktop/Coding/python/" + queryF, 'r')
                    for line in file.readlines:
                        print(Decode(line))
                if qurye == "append" :
                    file = open("Desktop/Coding/python/" + queryF, 'a')
                    queryW = raw_input("bgn>>> ")
                    file.write(FW(queryW))
                    file.close()
            if query[8:16] == "message.":
                tojoin = raw_input("A4>>> ")
                toJoin = "Desktop/Coding/python/" + tojoin + "_message.txt"
                if query[16:] == "create":
                    os.system("cd /Users/ben/Desktop/termfiles ; touch " + tojoin + "_message.txt")
                elif query[16:] == "seeall":
                    os.system("cd /Users/ben/Desktop/termfiles ; more " + toJoin)
                else:
                    while True:
                        file = open(toJoin,'r+')
                        nul = sum(1 for line in open(toJoin))
                        lines = file.readlines()
                        if nul != "0":
                            print(Decode(lines[nul-1]))
                        else:
                            print("\\Nothing to see here!")
                        TEXt = raw_input("bgn>>> ")
                        if TEXt == ".action.root.quit":
                            break
                        elif TEXt == ".action.message.seeall":
                            os.system("cd /Users/ben/Desktop/termfiles ; more " + toJoin)
                        else:
                            file.write(FW("usr_" + usrshrtd + " said " + TEXt + "\n"))
            if query[8:12] == "SGB.":
                os.system("open '/Users/ben/Desktop/AppleScript/ShitokiGo.app'")
                    
                    
if Qqq == "1" :
    while usrpswd[ysia] == pswd:
        query = raw_input("usr_" + usrshrtd + ">>> ")
        search(query, "00")
        if query[8:13] == "root." :
            Query = query[13:]
            if Query == "quit" :
                break
            if Query == "help" :
                os.system("more Desktop/Coding/python/terminalfile.txt")
            
if qqq == "0":
    print("Oops, that's not the right password!")
    
#    '.action' is how you start everything.
#    '.action.file' deals with files.
#   '.action.do', '.action.see', and '.action.SGB' are all searches.
#   '.action.root.quit' to quit!