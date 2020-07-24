FBn = raw_input("Enter a number: ")
while "quit" not in FBn.lower() and "exit" not in FBn.lower():
    FBn = int(FBn)
    FizzBuzz = ""
    if isinstance(FBn, int) is True:
        FBn += 1
        if str(float(FBn)/3)[str(float(FBn)/3).find(".")+1] == "0":
            FizzBuzz += "Fizz"
        if str(float(FBn)/5)[str(float(FBn)/5).find(".")+1] == "0":
            FizzBuzz += "Buzz"
        if FizzBuzz == "":
            FizzBuzz = FBn
        print(FizzBuzz)
    FBn = raw_input("Enter a number: ")