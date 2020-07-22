Ht = [ [ [ ["s", "m"], ["i", "t"] ], [ [ [",", "r"], "o"], [ ["c", "d"], "f"] ] ], 
[ [ ["n", [ [ ["j", "u"], ["!", "y"] ], ["p", ["'", "."] ] ] ], [ ["w", ["g", "h"] ], ["l", "k"] ] ], [ ["a", "e"], " "] ] ]
Encoded = raw_input("Enter the encoded binary here: ")
while " " not in Encoded:
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
            
        if isinstance(state, list) is True:
            y = y + 1
        else:
            x = x + (y + 1)
            y = 0
            Decoded = Decoded + state

    print(Decoded)
    Encoded = raw_input("Enter the encoded binary here: ")