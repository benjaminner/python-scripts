import time
cc = 0
dc = 0
now = time.time()
trntme = now + 30
stations = {'srrvyce':1,'tuomo':2,'leeo':3,'polutica':4,'orvochino':5,'loino':6,'ilumitcio':7}

po = raw_input("look at your current station. what is it's name? ")
if po in stations : 
    cc =  stations[po]
else :
    print("sorry, that is not a station")
    quit()
    
    
pp = raw_input("look at your destination station. what is it's name? ")
if pp in stations : 
    dc = stations[pp]
else :
    print("sorry, that is not a station")
    quit()
x = raw_input("type how many ways, or 'day pass'. ")
dist = abs(cc - dc)
if x == 'day pass':
    fareD = dist * 2
else :
    faree = dist * int(x)
    fare = faree / 1.35
    fareD = fare / (1+(int(x)-1)/10)
print ("your fare is $"),
print("{:.2f}".format(fareD))
if time.time() < trntme:
    print(":D you caught your train!")
else :
    print(":( you missed your train.")