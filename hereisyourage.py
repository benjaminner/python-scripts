import datetime
now = datetime.datetime.now()
dateofbirth =  raw_input("when were you born? ")
old = (int(now.year) - int(dateofbirth)-1)
print("Your age is:")
print(int(old))
futpstyr = raw_input("Enter a year and i'll tell you how old you will be then. ")
print((int(futpstyr) - now.year)+ int(old))