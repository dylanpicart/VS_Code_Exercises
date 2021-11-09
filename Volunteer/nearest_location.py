from list_of_locations import Location


self.pf = Location.preference(self, choice)
self.tl = Location.tell_location(self)

import random as rd

# This function outputs a random location in the given dictionary keys

def random_location():
    if self.pf(self.choice) == '1':
        print(rd.choice(self.fd_locations.keys()))
    elif self.pf(self.choice) == '2':
        print(rd.choice(self.hos_locations.keys()))
    elif self.pf(self.choice) == '3':
        print(rd.choice(self.cg_locations.keys()))
    else:
        print(f'Invalid input. Please try again.')
    
    
a = Location('Dylan')

a.random_location()