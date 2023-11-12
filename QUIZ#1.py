classCoffeeMachine:

def__init__(self):

self.water_capacity = 5

self.coffee_capacity = 3

def make_coffee(self):

self.water_capacity = self.water_capacity - 0.5

self.coffee_capacity = self.coffee_capacity - 0.5



return"Coffee Ready!"

def fill_water(self):

self.water_capacity = 5

def fill_coffee_chamber(self):

self.coffee_capacity = 3

def is_water_tank_empty(self):

if self.water_capacity == 0:

return(True)

def is_coffee_chamber_empty(self):

if self.coffee_capacity == 0:

return(True)