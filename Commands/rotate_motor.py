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
        logger.info("running Motor command")

    def execute(self):
        self.Phoenix_motor.go_up()

    def isFinished(self):
        return False
    
    def end(self, interrupted):
        self.Phoenix_motor.stop()

class Lower(commands2.Command):
     def __init__(self, Phoenix_motor: MotorSubsystem) -> None:
        super().__init__()
        self.Phoenix_motor = Phoenix_motor
    
     def execute(self):
        self.Phoenix_motor.go_down()

     def isFinished(self):
        return False
    
     def end(self, interrupted):
        self.Phoenix_motor.stop()



class StopMotor(commands2.Command):
     def __init__(self, Phoenix_motor: MotorSubsystem) -> None:
        super().__init__()
        self.Phoenix_motor = Phoenix_motor
    
     def initialize(self):
        logger.info("running StopMotor command")

     def execute(self):
        self.Phoenix_motor.stop()

     def isFinished(self):
        return False
    
     def end(self, interrupted):
        self.Phoenix_motor.stop()
    