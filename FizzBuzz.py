FBn = raw_input("Enter a number: ")
while "quit" not in FBn.lower() and "exit" not in FBn.lower():
    if isinstance(FBn, int) is True:
        FBn = int(FBn)
        FizzBuzz = ""
        FBn += 1
        if FBn % 3 == 0:
            FizzBuzz += "Fizz"
        if FBn % 5 == 0:
            FizzBuzz += "Buzz"
        if FizzBuzz == "":
            FizzBuzz = FBn
        print(FizzBuzz)
    FBn = raw_input("Enter a number: ")