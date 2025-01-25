import wpilib
import phoenix6
import commands2
import commands2.cmd
import wpimath.controller

from Subsystem.Phoenix_motor import MotorSubsystem

import constants
import logging

logger = logging.getLogger("aniyah")


class Lift(commands2.Command):
    def __init__(self, Phoenix_motor: MotorSubsystem) -> None:
        super().__init__()
        self.Phoenix_motor = Phoenix_motor
    
    def initialize(self):
        logger.info("running LIFT Motor command")
        self.Phoenix_motor.go_up()

    def isFinished(self):
        return True
    

class Lower(commands2.Command):
     def __init__(self, Phoenix_motor: MotorSubsystem) -> None:
        super().__init__()
        self.Phoenix_motor = Phoenix_motor
    
     def initialize(self):
        logger.info("running LOWER Motor command")
        self.Phoenix_motor.go_down()

     def isFinished(self):
        return True
    




class StopMotor(commands2.Command):
     def __init__(self, Phoenix_motor: MotorSubsystem) -> None:
        super().__init__()
        self.Phoenix_motor = Phoenix_motor
    
     def initialize(self):
        logger.info("running StopMotor command")
     def isFinished(self):
        return True
    
    
    