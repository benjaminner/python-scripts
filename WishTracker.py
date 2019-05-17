print ("If you want an infanite list, answer 'i' and to see all your items type '/see'")
wishestoadd = input("Wish list size(in items): ")
x = 0
items = []
wish = 0
if wishestoadd == 'i':
    wish = raw_input("Add Item: ")
    if wish == '/see':
        print("Your wish item(s): ")
        items.sort()
        print(items)    
    else:
        items.append(wish)
        x = x + 1
        print("Your wish item(s): ")
        items.sort()
        print(items)     
else: 
    while x < wishestoadd:
        wish = raw_input("Add Item: ")
        items.append(wish)
        x = x + 1
    print("Your wish item(s): ")
    items.sort()
    print(items)
