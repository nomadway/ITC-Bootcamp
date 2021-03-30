# Problem-6. Furniture:
# ﻿

# Household type, total area and furniture name listThe new house has no furniture at all.
# Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable: 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area, furniture name list.

class House():

    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.bed = 4
        self.wardrobe = 2
        self.table = 1.5

    def __Area(self): # private method 
        ##house style and total area
        print(f"The house is in {self.house_type} style, that has a total area of {str(self.house_area)} sqm.")

    def remaining_Area(self):
        '''Finding remaining area'''
        self.remain_area = self.house_area - self.bed - self.wardrobe - self.table
        print(f"Bed occupies {str(self.bed)} sqm, wardrobe takes up {str(self.wardrobe)} sqm, and table occupies {str(self.table)} sqm, and the remaining free area is {str(self.remain_area)} sqm.")

Gothic = House('Gothic',250)
Gothic._House__Area()
Gothic.remaining_Area()

class newHouse(House):
    def __init__(self, house_type, house_area):
        super().__init__(house_type, house_area) 
        
Modern_Urban = newHouse("Modern_Urban", 120)
Modern_Urban._House__Area() 
Modern_Urban.remaining_Area()






