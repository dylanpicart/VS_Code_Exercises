class Volunteer():
    def __init__(self, name, age, zip_code):
        self.name = name
        self.age = age
        self.zip_code = zip_code
        
            
    def user_zip(self):
        input_str = input('Please enter your zip code: ')
        print(input_str)
        if isinstance(self.zip_code, int) != True:
            raise TypeError('Invalid Input')
        if len(input_str) != 5:
            print("Please enter a 5 digit zip code!")
        return self.zip_code  
        
    def id_volunteer(self, town, state):
        self.town = town
        self.state = state
        if isinstance(self.town, str) != True or isinstance(self.state, str) != True:
            raise TypeError('Invalid Input')
        print(f'{self.name} is a volunteer from {self.town}, {self.state}!')
        
    # I could also move the preference function to list_of_locations
        
    
        ''' if choice == int, return true'''
    
dylan = Volunteer('Dylan', 25, 11003)
