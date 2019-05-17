Input = raw_input("Enter the kind of dimension you would like to enter: ")
Output = raw_input("Enter what you would like to get back:") 
if Input == "Radius" or "radius" :
     Radius = raw_input("Enter the radius of a circle: ")
     
     if Output == "Circumference" or "circumference" :
             Circumference = int(Radius) * 2 * 3.14159265358 
             print("The circumference of your circle is: ")
             print(Circumference)
             
     if Output == "Diameter" or "diameter" :
             Diameter = int(Radius) * 2 
             print("The diameter of your circle is: ")
             print(Diameter)
     
     if Output == "Area" or "area" :
             Area = (int(Radius) * int(Radius)) * 3.14159265358 
             print("The area of your circle is:")
             print(Area)

if Input == "Diameter" or "diameter" :
     Diameter = raw_input("Enter the radius of a circle: ")
     
     if Output == "Circumference" or "circumference" :
             Circumference = int(Diameter) * 3.14159265358 
             print("The circumference of your circle is: ")
             print(Circumference)
             
     if Output == "Radius" or "radius" :
             Radius = int(Diameter) / 2 
             print("The Radius of your circle is: ")
             print(Radius)
     
     if Output == "Area" or "area" :
             Area = ((int(Diameter) / 2) * (int(Diameter) / 2)) * 3.14159265358 
             print("The area of your circle is:")
             print(Area)




"Circumference" or "circumference" 
"Diameter" or "diameter"  
"Area" or "area"
"Radius" or "radius" 