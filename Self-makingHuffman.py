from collections import defaultdict
def start():
    Text = raw_input("Enter the text here: ")
    Letters = defaultdict(lambda:0)
    x = 0
    while x < len(Text) :
        Letters[Text[x]] += 1
        x += 1
    LettersVls = sorted(Letters.values())
    LettersKys = [v[0] for v in sorted(Letters.items(), key=lambda(k,v): (v,k))]
    
    x = 0
    while len(LettersKys) > 2 :
        Zero = LettersKys[0]
        One = LettersKys[1]
        Sum = LettersVls[0] + LettersVls[1]
        del Letters[Zero]
        del Letters[One]
        Letters[(Zero, One)] = Sum
    
        LettersVls = sorted(Letters.values())
        LettersKys = [v[0] for v in sorted(Letters.items(), key=lambda(k,v): (v,k))]
    
    return(LettersKys)
    

################################START OF MAIN PROGRAM###################################
Ht = start()

ToDo = raw_input("What would you like to do? ")
while "quit" not in ToDo.lower() and "exit" not in ToDo.lower() :
    ToDo = ToDo.lower()
    
    if ToDo == "r" or ToDo == "reenter" :
        Ht = start()
    elif ToDo == "p" or ToDo == "print" :
        print(Ht)
    elif ToDo == "e" or ToDo == "encode" :
        Decoded = raw_input("Enter the text to be encoded here: ")
        StrHt = str(Ht)
        StrHt = StrHt[1:len(StrHt)-1]
        a = 0
        Ht0 = " "
        Ht1 = " "
        HtA = ""
        while a < len(Decoded) and Decoded[a] in StrHt:
            while Ht1 != "": 
                x = 0
                y = 0
                z = 0
                while x < len(StrHt):
                    if StrHt[x] == "(":
                        y += 1
                    elif StrHt[x] == ")":
                        y -=1
                    if y == 0 and z == 0:
                        Ht0 = StrHt[:x+1]
                        Ht1 = StrHt[x+3:]  
                        z += 1  
                    x += 1 
                if Decoded[a] in Ht0 and Ht1 != "":
                    StrHt = Ht0
                    HtA += "0"
                if Decoded[a] in Ht1:
                    StrHt = Ht1
                    HtA += "1"
                print(StrHt[1:len(StrHt)-1])
            if Decoded[a] == StrHt[2]:
                HtA += "0"
            elif Decoded[a] == StrHt[7]:
                HtA += "1"
            elif Decoded[a] == StrHt[8] and StrHt[1] != "(":
                HtA += "10"
            elif Decoded[a] == StrHt[13]:
                HtA += "11"
            elif Decoded[a] == StrHt[3]:
                HtA += "00"
            elif Decoded[a] == StrHt[8]:
                HtA += "01"
            Ht0 = " "
            Ht1 = " "
            print("It is incementing a!")
            print(StrHt)
            StrHt = str(Ht)
            StrHt = StrHt[1:len(StrHt)-1]
            a += 1
        print(HtA)
    elif ToDo == "d" or ToDo == "decode" or "0" in ToDo or "1" in ToDo:
        if "0" in ToDo or "1" in ToDo:
            Encoded = ToDo
        else:
            Encoded = raw_input("Enter the encoded binary here: ")
        while "quit" not in Encoded.lower() and "exit" not in Encoded.lower() :
            #digit to start reading from
            x = 0
            #length of current letter
            y = 0
            Decoded = ""
            while x+y < len(Encoded):
                if y == 0:
                    state = Ht[int(Encoded[x])]
                if y == 1:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])]
                if y == 2:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])][int(Encoded[x+2])]
                if y == 3:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])][int(Encoded[x+2])][int(Encoded[x+3])]
                if y == 4:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])][int(Encoded[x+2])][int(Encoded[x+3])][int(Encoded[x+4])]
                if y == 5:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])][int(Encoded[x+2])][int(Encoded[x+3])][int(Encoded[x+4])][int(Encoded[x+5])]
                if y == 6:
                    state = Ht[int(Encoded[x])][int(Encoded[x+1])][int(Encoded[x+2])][int(Encoded[x+3])][int(Encoded[x+4])][int(Encoded[x+5])][int(Encoded[x+6])]
                    
                if isinstance(state, tuple) is True:
                    y += 1
                else:
                    x = x + (y + 1)
                    y = 0
                    Decoded = Decoded + state
            
            print(Decoded)
            
            Encoded = raw_input("Enter the encoded binary here: ")
    else: 
        print("Sorry, That function is temporarily disabled.")
    ToDo = raw_input("What would you like to do? ")