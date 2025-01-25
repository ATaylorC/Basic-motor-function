import wpilib
import phoenix6
import commands2

import wpilib
import phoenix6
import commands2

from constants import ELEC
from constants import MECH

class MotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.phoenixmotor = phoenix6.hardware.TalonFX(ELEC.Phoenix_motor_CAN_ID)
        self.controller = wpilib.XboxController

    def go_up(self):
        self.phoenixmotor.set(MECH.Phoenix_motor_speed)

    def go_down(self):
        self.phoenixmotor.set(-MECH.Phoenix_motor_speed)

    def stop(self):
        self.phoenixmotor.set(0)

    def is_stopped(self):
        motor_speed = self.motor.get()
        if motor_speed == 0:
            return True 
        else:
            return False