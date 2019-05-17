from tkinter import Tk, simpledialog, messagebox
import webbrowser

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n') 
            country, city = line.split('/')
            the_world[country] = city
            
def gather_push():
    with open('unchecked_data.txt') as file:
        for line in file:
            line = line.rstrip('\n') 
            country, city = line.split('/')
            push[country] = city
            
            with open ('capital_data.txt', 'a') as file:
                file.write('\n' + country + '/' + city)
                
        open('unchecked_data.txt', 'w').close()
                
def write_to_file(country_name, city_name):
    with open ('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)
        
def write_to_uncheckedfile(country_name, city_name):
    with open ('unchecked_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)          
          

print('Ask the Expert - Capital Cities of the World')

root = Tk()
root.withdraw
the_world = {}
push = {}

read_from_file()


while True:
    query_country = simpledialog.askstring('Country', 'Type the name of a country: ')
    
    if query_country == 'push':
          password = simpledialog.askstring('Password',
                                                       'Please enter the password ' + 
                                                                                     'If you do not know the password, type "?"')
          if password == "thiskid":
              
              messagebox.showinfo('Push', 
                                         'Pushing...')
                                     
              gather_push()
              
              messagebox.showinfo('Push', 
                                         'Pushed!')  
          else:
              root.destroy()
    
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer', 
                                     'The capital city of ' + query_country + ' is ' + result + '!')                                
    elif query_country != 'push' :
      
         webbrowser.open('https://www.google.com/search?q=capital+city+of+' + query_country)
         new_city = simpledialog.askstring('Teach me!',
                                                       'Read from the browser! ' + 
                                                                          'What is the capital city of ' + query_country + '?')
                                                                         
         password = simpledialog.askstring('Password',
                                                      'Please enter the password ' + 
                                                                                    'If you do not know the password, type "?"')
         if password == "thiskid":
             the_world[query_country] = new_city
             write_to_file(query_country, new_city)
         else:
             write_to_uncheckedfile(query_country, new_city)
        
        
root.mainloop()