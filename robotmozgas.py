from pybricks.tools import wait, StopWatch, DataLog
from pybricks.parameters import Port, Stop, Direction, Button, Color
def elso_feladat(robot):
    robot.straight(30)
    robot.straight(-30)
    robot.turn(90)
    robot.turn(-90)
    

def mozgas2(robot):
    robot.drive(100, 0)
    robot.reset()
    wait(1)
    robot.drive(100, 0)
    

    