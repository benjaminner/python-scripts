import datetime
current = datetime.datetime.now()
os.system("git add .")
os.system('git commit -m ' + '"' + current.strftime("%B") + " " + current.strftime("%d") + ' Update!"')
os.system("git push")