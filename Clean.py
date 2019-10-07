import os

message = raw_input("What would you like your commit message to be? ")

os.system("git add .")
os.system("git commit -m " + '"' + message + '"')
os.system("git push")