cc = 0
dc = 0
po = raw_input("look at your current station. what is it's name? ")
if po == 'srrvyce':
    cc = 1
elif po == 'tuomo':
    cc = 2
elif po == 'leeo':
    cc = 3
elif po == 'polutica':
    cc = 4
elif po == 'orvochino':
    cc = 5
elif po == 'loino':
    cc = 6
elif po == 'ilumitcio':
    cc = 7
else :
    print("sorry, that is not a station")
    quit()
pp = raw_input("look at your destination station. what is it's name? ")
if pp == 'srrvyce':
    dc = 1
elif pp == 'tuomo':
    dc = 2
elif pp == 'leeo':
    dc = 3
elif pp == 'polutica':
    dc = 4
elif pp == 'orvochino':
    dc = 5
elif pp == 'loino':
    dc = 6
elif pp == 'ilumitcio':
    dc = 7
else :
    print("sorry, that is not a station")
    quit()
dist = abs(cc - dc)
fare = dist * 1.05
print ("your fare is $"),
print("{:.2f}".format(fare))