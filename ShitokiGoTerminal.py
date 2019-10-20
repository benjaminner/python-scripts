print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 
import webbrowser

while True:
    query = raw_input(">>> ")
    if query[:3] == "lgn" :
        login = query[3:]
        terminR = open("terminalfile.txt","a")
        terminR.write(login)
        termin = open("terminalfile.txt","r")   
        print(termin.read())
        
    if query[:8] == ".action." :
        if query[8:11] == "do." :
            action = query[11:]
            webbrowser.open("https://www.youtube.com/results?search_query=" + action)
        if query[8:14] == "speak." :
            saY = query[14:]
            os.system("say " + saY)
    if query == "quit()" :
            break