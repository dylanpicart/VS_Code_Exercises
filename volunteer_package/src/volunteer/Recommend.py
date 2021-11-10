from volunteer_info import Volunteer
from list_of_locations import Location

# we want to reference both the volunteer class and the location 

class Recommend(Volunteer):
    def __init__(self, name, age, zip_code):
        super().__init__(name, age, zip_code)
        
    
    def recommend_place(self):
        user = input("Is this location where you'd like to volunteer at?\n Enter Y or N: ")
        if user == 'Y':
            print(f"{self.name} of {self.town}, {self.state} would like to volunteer here!")
        elif user == 'N':
            print(f"Please use our random location finder!")
        else:
            print("Please use Y or N for your choice and try again.")

dylan = Recommend('Dylan', 25, 11003)
dylan.id_volunteer('Elmont', 'NY')
dylan.recommend_place()

# If user inputs N

d = Location('Dylan')
d.preference(1)
d.random_location()