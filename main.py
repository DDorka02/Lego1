#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import robotmozgas


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
jm = Motor(Port.B)
bm = Motor(Port.C)
km = Motor(Port.A)
ts = TouchSensor(Port.S1)
gs = GyroSensor(Port.S2)
cs = ColorSensor(Port.S3)
us = UltrasonicSensor(Port.S4)
robot = DriveBase(bm,jm,45,142)

# Write your program here.
#robotmozgas.elso_feladat(robot)
robotmozgas.mozgas2(robot)
ev3.speaker.beep()