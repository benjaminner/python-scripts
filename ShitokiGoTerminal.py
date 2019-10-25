print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 
import webbrowser
import getpass
os.system("say Hello, and welcome to the Shitoki Go! interactive terminal SGIT!")
usrpswd = {"Ben" : "brainlakeadmin1", }
usrshrt = {"Ben" : "ben", }
ysia = raw_input("Brainlake Username: ")
pswd = getpass.getpass("Brainlake Password: ")

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
                if query[13:] == "create":
                    os.system("cd /Users/ben/Dropbox/Ben/python/termfiles ; touch " + queryF)
                if query[13:] == "erase":
                    password = getpass.getpass("Pswd>>> ")
                    if password == "securebrainlakeadmin":
                        tst = open("/Users/ben/Desktop/termfiles/" + queryF, 'w')
                        tst.close()
                if query[13:] == "read":
                    os.system("cd /Users/ben/Desktop/termfiles ; more " + queryF)
                if query[13:] == "append" :
                    file = open("/Users/ben/Desktop/termfiles/" + queryF, 'a')
                    queryW = raw_input("bgn>>> ")
                    file.write(queryW)
                    file.close()
            if query[8:16] == "message.":
                tojoin = raw_input("A4>>> ")
                if query[16:] == "create":
                    os.system("cd /Users/ben/Desktop/termfiles ; touch " + tojoin + "_message.txt")
                else:
                    toJoin = "/Users/ben/Desktop/termfiles/" + tojoin + "_message.txt"
                    while True:
                        file = open(toJoin,'r+')
                        nul = sum(1 for line in open(toJoin))
                        lines = file.readlines()
                        print(lines[nul-1])
                        TEXt = raw_input("bgn>>> ")
                        if TEXt == ".action.root.quit":
                            break
                        file.write("\n" + "usr_" + usrshrt[ysia] + ">>> " + TEXt)
                    
                    
while usrpswd[ysia] == pswd:
    query = raw_input(">>> ")
    search(query, "00")
    if query[8:13] == "root." :
        Query = query[13:]
        if Query == "quit" :
            break
        if Query == "help" :
            print("'.action.root.quit' to quit!")