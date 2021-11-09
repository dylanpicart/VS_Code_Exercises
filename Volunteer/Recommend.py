from volunteer_info import Volunteer
from list_of_locations import Location
from nearest_location import random_location as rl

# we want to reference both the volunteer class and the location 

class Recommend(Volunteer):
    def __init__(self, name, zip_code):
        super().__init__(location)
        self.name = name
        self.zip_code = zip_code
     
        u_id = Volunteer.id_volunteer(self, town, state)
    
    def recommend_place(self):
        user = input("Is this location where you'd like to volunteer at?\n Enter Y or N: ")
        if user == 'Y':
            print(f"{self.name} of {self.town}, {self.state} would like to volunteer at {address}!")
        elif user == 'N':
            print(f"{self.name} of {self.town}, {self.state} we'd like to recommend {self.rl}")
        else:
            print("Please use Y or N for your choice and try again.")

dylan = Volunteer('Dylan', 25, 11003)

