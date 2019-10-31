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
                    os.system("cd /Users/ben/Dropbox/Ben/python/termfiles ; touch " + queryF)
                if qurye == "erase":
                    password = getpass.getpass("Pswd>>> ")
                    if password == "securebrainlakeadmin":
                        tst = open("/Users/ben/Desktop/termfiles/" + queryF, 'w')
                        tst.close()
                if qurye == "read":
                    os.system("cd /Users/ben/Desktop/termfiles ; more " + queryF)
                if qurye == "append" :
                    file = open("/Users/ben/Desktop/termfiles/" + queryF, 'a')
                    queryW = raw_input("bgn>>> ")
                    file.write(queryW)
                    file.close()
            if query[8:16] == "message.":
                tojoin = raw_input("A4>>> ")
                toJoin = "/Users/ben/Desktop/termfiles/" + tojoin + "_message.txt"
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
                            print(lines[nul-1])
                        else:
                            print("\\Nothing to see here!")
                        TEXt = raw_input("bgn>>> ")
                        if TEXt == ".action.root.quit":
                            break
                        elif TEXt == ".action.message.seeall":
                            os.system("cd /Users/ben/Desktop/termfiles ; more " + toJoin)
                        else:
                            file.write("usr_" + usrshrtd + " said " + TEXt + "\n")
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
                os.system("more /Users/ben/Desktop/termfiles/terminalfile.txt")
            
if qqq == "0":
    print("Oops, that's not the right password!")