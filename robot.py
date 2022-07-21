# Jannatul Alia task code July 2022
from re import compile, I, X, finditer
from coordinate import Coordinate

#constant strings
CONST_CMD_PLACE = "PLACE"
CONST_CMD_REPORT = "REPORT"
CONST_CMD_RIGHT = "RIGHT"
CONST_CMD_LEFT = "LEFT"
CONST_CMD_MOVE = "MOVE"
    
CONST_CMD_NAME = "cmd"
    
CONST_DIR_NORTH = "NORTH"
CONST_DIR_EAST = "EAST"
CONST_DIR_SOUTH = "SOUTH"
CONST_DIR_WEST = "WEST"


DIRECTIONS = {
    CONST_DIR_WEST: 0,
    CONST_DIR_NORTH: 90,
    CONST_DIR_EAST: 180,
    CONST_DIR_SOUTH: 270,
}

ROTATIONS = {
    CONST_CMD_LEFT: -90,
    CONST_CMD_RIGHT: 90,
}

class Robot(object):
    is_placed = False
    direction = None
    table = None

    
    coordinate = None
    #group based on the input pattern
    expression = r"""((?:\s)*                                   #space
                      (?P<cmd>MOVE|LEFT|RIGHT|REPORT|PLACE)     #cmd
                      ((?:\s?)                                  #space either no space or once 
                      (?P<x>\d),(?P<y>\d),)*                    #coordinates zero or more
                      (?P<dir>NORTH|EAST|SOUTH|WEST)*           #direction zero or more
                      )?                                        #group matched zero or one
                  """
                     
    #allow verbose pattern / with comments, newlines (readable).
    pattern = compile(expression, X)
    
    
    def __init__(self, table):
        print("CREATING ROBOT")
        self.table = table
        
    def parse_command(self, input_command):
        #using finditer due to reusing same pattern and multiple matches
        matches = finditer(self.pattern, input_command)
        for match in matches:
            if match is not None:
                if match.group(CONST_CMD_NAME) == CONST_CMD_PLACE:
                    self.set_command(CONST_CMD_PLACE)
                    self.set_coordinate(int(match.group("x")), int(match.group("y")))
                    self.set_direction(match.group("dir"))
                    self.set_placed(True)
                if self.is_placed:
                    if match.group(CONST_CMD_NAME) == CONST_CMD_MOVE:
                        #set movement
                        if self.get_direction() == CONST_DIR_NORTH:
                            #add one unit towards +y / NORTH
                            self.set_coordinate(self.get_coordinate().x, self.get_coordinate().y +1)
                        elif self.get_direction() == CONST_DIR_WEST:
                            #add one unit towards -x / WEST
                            self.set_coordinate(self.get_coordinate().x-1, self.get_coordinate().y)
                        elif self.get_direction() == CONST_DIR_SOUTH:
                            #add one unit towards -y / SOUTH
                            self.set_coordinate(self.get_coordinate().x, self.get_coordinate().y-1)
                        elif self.get_direction() == CONST_DIR_EAST:
                            #add one unit towards X / WEST
                            self.set_coordinate(self.get_coordinate().x+1, self.get_coordinate().y)
                        
                    if match.group(CONST_CMD_NAME) == CONST_CMD_LEFT or match.group(CONST_CMD_NAME) == CONST_CMD_RIGHT:
                        #rotate the direction of the robot
                        new_direction_value = DIRECTIONS.get(self.get_direction())+ ROTATIONS.get(match.group(CONST_CMD_NAME))
                        #set the new direction
                        self.set_direction(dict((new_val,new_k) for new_k,new_val in DIRECTIONS.items()).get(new_direction_value))
                    if match.group(CONST_CMD_NAME) == CONST_CMD_REPORT:
                        self.report()
                else:
                    print("PLEASE PLACE THE ROBOT FIRST")
                    
    def set_command(self, command):
        self.command = command
        
    def set_coordinate(self, x, y):
        coordinate = Coordinate(x,y)
        if self.table.within_boundary(coordinate):
            self.coordinate= coordinate
        
    def get_coordinate(self):
        return self.coordinate
        
    def set_placed(self, status):
        self.is_placed=True
        
    def set_direction(self, direction):
        self.direction=direction 
        
    def get_direction(self):
        return self.direction
    
            
    def report(self):
        print ("Result:")
        print(self.coordinate.x,self.coordinate.y,self.direction )
        
    
    
        
        