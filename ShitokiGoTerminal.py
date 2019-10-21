print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 
import webbrowser
os.system("say Hello, and welcome to the Shitoki Go! interactive terminal SGIT!")

while True:
    query = raw_input(">>> ")
   # if query[:3] == "lgn" :
      #  login = query[3:]
       # terminR = open("terminalfile.txt","a")
        #terminR.write(login)
        #termin = open("terminalfile.txt","r")   
        #print(termin.read())
        
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
        if query[8:13] == "root." :
            Query = query[13:]
            if Query == "quit" :
                break
            elif Query == "help" :
                print("'.action.root.quit' to quit!")
        else:
            print("Sorry, that's not a command!")
    else:
        print("Sorry, that's not a command!")