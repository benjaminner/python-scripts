Word = raw_input("Please give me a word. ")
print(len(Word) * "_")
Letter = raw_input("Please give me a letter. ")
if (Letter in Word) :
    print("You're a winner")