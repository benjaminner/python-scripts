cipher_dictionary = {
'a' : 'c',
'b' : 'o',
'c' : 'r',
'd' : 'n',
'e' : 'a',
'f' : 'v',
'g' : 'i',
'h' : 'u',
'i' : 's',
'j' : 'e',
'k' : 'l',
'l' : 'y',
'm' : 'k',
'n' : 'd',
'o' : 'p',
'p' : 't',
'q' : 'q',
'r' : 'b',
's' : 'w',
't' : 'j',
'u' : 'x',
'v' : 'z',
'w' : 'f',
'x' : 'm',
'y' : 'g',
'z' : 'h',
}

inputmessage = ""
while inputmessage != "(quit)":
    printe = ""
    inputmessage = str(input("Enter a message: ")).lower()
    
    if "[" in inputmessage and "]" in inputmessage:

        left = inputmessage.find('[')
        leftone = left + 1

        s2 = inputmessage[leftone:]

        right = s2.find(']')

        DeEn = s2[:right]
        inputmessage = inputmessage[0:left]
    
    else:
        DeEn = "e"
    
    if DeEn == "d":
        for character in inputmessage:
            if character in cipher_dictionary:
                for key, value in cipher_dictionary.items(): 
                     if character == value: 
                         printe = printe + key
            else:
                printe = printe + character 
            
    else:
        for character in inputmessage:
            if character in cipher_dictionary:
                printe = printe + cipher_dictionary[character]
            else:
                printe = printe + character 
                
    if inputmessage != "(quit)":
        print(printe)