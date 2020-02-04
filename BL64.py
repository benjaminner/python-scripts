import playsound 
import webbrowser
import os
import tkinter
out_of_space = no
playsound.playsound("/Users/ben/Desktop/BL64/n64-startup.mp3",True)
print("Brainlake 64")
print("Copyright Brainlake Inc, 2019")
while True:
    playsound.playsound("/Users/ben/Desktop/BL64/3-05-world-map-5-the-sky-.mp3",True)
    def get_size(start_path = '.'):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size
    if get_size("/Users/ben/Desktop/BL64") > 64000000:
        out_of_space = yes
    else: 
        out of space = no 