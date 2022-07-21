# Jannatul Alia task code July 2022
from table import Table
from robot import Robot

# create Table
table = Table(5,5)

#prompt available command
print("\nStart PLACE & MOVE YOUR ROBOT!")
command = input()

#create robot
robot = Robot(table)
robot.parse_command(command)