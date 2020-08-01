import datetime as dt
inputt = ""
outputt = ""
sequence = ["", "", "", ""]
ops = ["1", "2", "3", "4", "5", "6"]

for n in range(4):
    while not sequence[n] in ops:
        strdt = str(dt.datetime.now())
        sequence[n] = strdt[len(strdt)-1]
    ops.remove(sequence[n])

print("Sequences that follow are four digits, numbers 1-6, and no numbers repeat.")

while outputt != "HHHH":
    inputt = raw_input("Enter a sequence here: ")
    outputt = ""
    for x in range(4):
        if inputt[x] == sequence[x]:
            outputt += "H"
        elif inputt[x] in sequence:
            outputt += "B"
        else:
            outputt += "-"
    print(outputt)
print("You won!")