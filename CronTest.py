import datetime
time = datetime.datetime.now()
file = open("123!.txt", 'a')
file.write(str(time.hour) + ":" + str(time.minute))
file.write("\n")
file.close()