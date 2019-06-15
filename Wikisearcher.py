import webbrowser 
x = 0 

for x in [ "0" ] : 
    WikiSearch = raw_input("Search the wiki: ") 

    webbrowser.open_new_tab("https://www.wikipedia.org/wiki/" + WikiSearch)
