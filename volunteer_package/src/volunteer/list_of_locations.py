import random as rd
class Location():
    def __init__(self, name):
        self.name = name
        self.choice = None
            
        # create a dictionary to reference
        # if user specified 1, 2, or 3, utilize location from different dictionaries
        self.fd_locations ={"Food Bank NYC":"355 Food Center Dr, Bronx, NY",
                        "Long Island FDC":"58 Hilton Ave, Hempstead, NY", 
                        "The Campaign Against Hunger":"2010 Fulton St, Brooklyn, NY"}

        self.hos_locations = {"NYU Langone":"550 1st Ave, New York, NY",
                        "Jamaica Hospital":"8900 Van Wyck Expy, Richmond Hill, NY",
                        "Morris Heights Health Center":"1930 Andrews Ave S, Bronx, NY"}

        self.cg_locations = {"Centennial Gardens":"251 Floral Pkwy, Floral Park, NY",
                        "Crossroads Farm":"480 Hempstead Ave, Malverne, NY", 
                        "Highland Park":"398 Jamaica Ave, Brooklyn, NY"}
          
          
    def preference(self, choice):
        self.choice = choice
        # create a default case
        is_int = False   
        while is_int == False:
            self.choice = input('Choose a preference:\n 1: Food Drive\n 2: Hospital\n 3: Community Garden\n ')
            if self.choice == int:
                is_int = True
            if self.choice == '1':
              print(f'{self.name} would like to work at the Food Drive.')
            elif self.choice == '2':
              print(f'{self.name} would like to work at the Hospital.')
            elif self.choice == '3':
              print(f'{self.name} would like to work at the Community Garden.')
            elif self.choice != '1' or self.choice != '2' or self.choice != '3':
              print('Please input 1, 2, or 3 for your options & run again.')
            break        


    '''Let's create nested statements under make_recommendation().
    We want to access the preference function and apply different dictionary
    choices based on what the user chose in the info method.'''

    
    def tell_location(self):
        user_input = input("Where would you like to work? ")
        if self.choice == '1':
            keys = list(self.fd_locations.keys())
            print(keys)
            if(user_input == "Food Bank NYC"):
                address = self.fd_locations[user_input]
                print(f"Food Bank NYC is located at {address}")
            elif(user_input == "Long Island FDC"):
                address = self.fd_locations[user_input]
                print(f"Long Island FDC is located at {address}")   
            elif(user_input == "The Campaign Against Hunger"):
                address = self.fd_locations[user_input]
                print(f"The Campaign Against Hunger is located at {address}")
            else:
                print(f'Sorry, we could not find this location.\n Please check your spelling and try again.')
        
        elif self.choice == '2':
            keys = list(self.hos_locations.keys())
            print(keys)
            if(user_input == "NYU Langone"):
                address = self.hos_locations[user_input]
                print(f"NYU Langone is located at {address}")
            elif (user_input == "Jamaica Hospital"):
                address = self.hos_locations[user_input]
                print(f"Jamaica Hospital is located at {address}")
            elif (user_input == "Morris Heights Health Center"):
                address = self.hos_locations[user_input]
                print(f"Morris Heights Health Center is located at {address}")
            else:
                print(f'Sorry, we could not find this location.\n Please check your spelling and try again.')
        
        elif self.choice == '3':
            keys = list(self.cg_locations.keys())
            print(keys)
            if(user_input == "Centennial Gardens"):
                address = self.cg_locations[user_input]
                print(f"Centennial Gardens is located at {address}")
            elif (user_input == "Crossroads Farm"):
                address = self.cg_locations[user_input]
                print(f"Crossroads Farm is located at {address}")
            elif (user_input == "Highland Park"):
                address = self.cg_locations[user_input]
                print(f"Highland Park is located at {address}")
            else:
                print(f'Sorry, we could not find this location.\n Please check your spelling and try again.')
                
        
    def random_location(self):
        if self.choice == '1':
            keys = list(self.fd_locations.keys())
            print(rd.choice(keys))
        elif self.choice == '2':
            keys = list(self.hos_locations.keys())
            print(rd.choice(keys))
        elif self.choice == '3':
            keys = list(self.cg_locations.keys())
            print(rd.choice(keys))
        else:
            print(f'Invalid input. Please try again.')
      
      
b = Location('Dylan')
b.preference(1)
b.tell_location()
