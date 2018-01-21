
cc = 0
dc = 0

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

dist = abs(cc - dc)
fare = dist * 1.05
print ("your fare is $"),
print("{:.2f}".format(fare))