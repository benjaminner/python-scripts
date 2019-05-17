pi = 3.14159265358
import math
Input = raw_input('Enter the kind of dimension you would like to enter( "Circumference", "Diameter" , "Area" , "Radius" ): ')
Output = raw_input('Enter what you would like to get back( "Circumference", "Diameter" , "Area" , "Radius" ): ') 
if Input in ["Radius" , "radius"] :
     Radius = raw_input("Enter the radius of a circle: ")
     
     if Output in ["Circumference" , "circumference"] :
             Circumference = int(Radius) * 2 * pi 
             print("The circumference of your circle is:")
             print(Circumference)
             
     if Output in ["Diameter" , "diameter"] :
             Diameter = int(Radius) * 2 
             print("The diameter of your circle is:")
             print(Diameter)
     
     if Output in ["Area" , "area"] :
             Area = (int(Radius) **2) * pi
             print("The area of your circle is:")
             print(Area)

if Input in ["Diameter" , "diameter"] :
     Diameter = raw_input("Enter the diameter of a circle: ")
     
     if Output in ["Circumference" , "circumference"] :
             Circumference = int(Diameter) * pi 
             print("The circumference of your circle is:")
             print(Circumference)
             
     if Output in ["Radius" , "radius"] :
             Radius = int(Diameter) / 2 
             print("The Radius of your circle is:")
             print(Radius)
     
     if Output in ["Area" , "area"] :
             Area = ((int(Diameter) / 2) **2) * pi 
             print("The area of your circle is:")
             print(Area)
             
if Input in ["Area" , "area"] :
    Area = raw_input("Enter the area of a circle: ")
    
    if Output in ["Circumference" , "circumference"] :
            Circumference = math.sqrt( int(Area) / pi) * 2 * pi
            print("The circumference of your circle is:")
            print(Circumference)
            
    if Output in ["Diameter" , "diameter"] :
            Diameter = math.sqrt(int(Area) / pi) * 2
            print("The diameter of your circle is:")
            print(Diameter)
    
    if Output in ["Radius" , "radius"] :
            Radius = math.sqrt(int(Area) / pi)
            print("The area of your circle is:")
            print(Radius)

print("Thank you for using Circles.py!")

#[ "Circumference" , "circumference" ] 
#[ "Diameter" , "diameter" ] 
#[ "Area" , "area" ]
#[ "Radius" , "radius" ]