print('Hello, and welcome to the Shitoki Go! interactive terminal(SGIT)!')
import os 


while True:
    query = raw_input(">>> ")
    if query[:3] == "lgn" :
        login = query[3:]
        terminR = open("terminalfile.txt","a")
        termin = open("terminalfile.txt","r")
        terminR.write(login)   
        print(termin.read())
        
    if query[:1] == "." :
        if query[1:11] == "action.do." :
            action = query[11:]
    if query == "quit()" :
            break