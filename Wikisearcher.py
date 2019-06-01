x = 0 

for x in [ "0" ] : 
    import webbrowser 
    WikiSearch = raw_input("Search the wiki: ") 

    webbrowser.open_new_tab("https://www.wikipedia.org/wiki/" + WikiSearch)
    