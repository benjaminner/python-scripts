import os

message = raw_input("What would you like your commit message to be? ")

os.system("git status")
print("#############The files above in red will be updated#############")
os.system("git add .")
os.system("git commit -m " + '"' + message + '"')
os.system("git push")


# cd
# ~/.bash_profile