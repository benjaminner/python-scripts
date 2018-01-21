import datetime
now = datetime.datetime.now()
dateofbirth =  raw_input("when were you born?")
print("Your age is:")
print(int(now.year) - int(dateofbirth)-1)