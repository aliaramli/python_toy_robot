# Jannatul Alia task code July 2022
from coordinate import Coordinate
class Table(object):
    
    # On constructing the table, should define the heigth and width
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # Check if item placed on the table is within the boundary
    # Reuse the min range width value instead of using magic number
    def within_boundary(self, coordinate):
        if (coordinate.x  >= min(range(self.width)) and coordinate.x < self.width) and (coordinate.y >= min(range(self.height)) and coordinate.y < self.height) :
            return True
        else : 
            print("ENCOUNTERED INVALID COORDINATES PLACEMENT")
            return False