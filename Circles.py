pi = 3.14159265358
import math
Input = raw_input('Enter the kind of dimension you would like to enter( "Circumference", "Diameter" , "Area" , "Radius" ): ')
Output = raw_input('Enter what you would like to get back( "Circumference", "Diameter" , "Area" , "Radius" ): ') 

radius = ["Radius" , "radius", "r"]
circumference = ["Circumference" , "circumference", "c"]
diameter = ["Diameter" , "diameter", "d"]
area = ["Area" , "area", "a"]

if Input in radius :
     Radius = raw_input("Enter the radius of a circle: ")
     
     if Output in circumference :
             Circumference = int(Radius) * 2 * pi 
             print("The circumference of your circle is:")
             print(Circumference)
             
     if Output in diameter :
             Diameter = int(Radius) * 2 
             print("The diameter of your circle is:")
             print(Diameter)
     
     if Output in area :
             Area = (int(Radius) **2) * pi
             print("The area of your circle is:")
             print(Area)

if Input in diameter :
     Diameter = raw_input("Enter the diameter of a circle: ")
     
     if Output in circumference :
             Circumference = int(Diameter) * pi 
             print("The circumference of your circle is:")
             print(Circumference)
             
     if Output in radius :
             Radius = int(Diameter) / 2 
             print("The Radius of your circle is:")
             print(Radius)
     
     if Output in area :
             Area = ((int(Diameter) / 2) **2) * pi 
             print("The area of your circle is:")
             print(Area)
             
if Input in area :
    Area = raw_input("Enter the area of a circle: ")
    
    if Output in circumference :
            Circumference = math.sqrt( int(Area) / pi) * 2 * pi
            print("The circumference of your circle is:")
            print(Circumference)
            
    if Output in diameter :
            Diameter = math.sqrt(int(Area) / pi) * 2
            print("The diameter of your circle is:")
            print(Diameter)
    
    if Output in radius :
            Radius = math.sqrt(int(Area) / pi)
            print("The area of your circle is:")
            print(Radius)
            
if Input in circumference :
    Circumference = raw_input("Enter the circumference of a circle: ")
    
    if Output in area :
            Area = (((int(Circumference) / pi) / 2 ) **2 ) * pi
            print("The area of your circle is:")
            print(Area)
            
    if Output in diameter :
            Diameter = int(Circumference) / pi 
            print("The diameter of your circle is:")
            print(Diameter)
    
    if Output in radius :
            Radius = (int(Circumference) / pi) / 2
            print("The area of your circle is:")
            print(Radius)

print("Thank you for using Circles.py!")