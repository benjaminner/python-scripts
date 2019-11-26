#import keyboard
Outs = 0
Inning = 0
Inning_Half = 0
Runs_Computer = 0
Runs_Player = 0
Counter = 0
DfP = 0
Hit = "No!"
Strikes = 0

while Inning != 10 and Counter == 0 :
    print(Runs_Computer)
    print("\n" + Runs_Player)
    while True: 
        String1 = DfP * " "
        String2 = (8 - DfP) * " "
        print("o" + String1 + "." + String2 + "l")
        if keyboard.is_pressed('s'):
            if DfP == 8:
                Hit = "Yes!"
        DfP = DfP + 1
        if DfP == 9 and Hit == "No!":
            Strikes = Strikes + 1 
        if Strikes == 3:
            Outs = Outs + 1
            Strikes == 0
        if Outs == 3:
            Inning_Half = Inning_Half + 1
            Outs = 0
        if Inning_Half == 2:
            Inning = Inning + 1
            Inning_Half = 0
        if Hit == "Yes!":
            Runs_Player = Runs_Player + 1 
        time.sleep(.5)