x = 0 

for x = 0 : 
    import webbrowser 
    WikiSearch = raw_input("Search the wiki!") 

    webbrowser.open_new_tab("https://www.wikipedia.org/wiki/" + WikiSearch)
    
    Go_Again = raw_input("Press enter if you would like to go again! ")
    if Go_Again != "" :
        x = 1