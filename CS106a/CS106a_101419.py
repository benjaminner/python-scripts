s = raw_input("Catiffy: ")

def catty(s):
    result = ''
    for i in range(len(s)):
        char = s[i]
        if char in 'catCAT' :
            result += s[i]
    return result
    
print(catty(s))