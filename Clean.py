import os

os.system("git status")
print("#############The files above in red will be updated#############")
message = raw_input("What would you like your commit message to be? ")
check = raw_input("Are you sure?(y/n) ")
if check.lower() == "y":
    os.system("git diff")
    os.system("git add .")
    os.system("git commit -m " + '"' + message + '"')
    os.system("git push")


# cd
# ~/.bash_profile