import wpilib
import phoenix6
import commands2

import wpilib
import phoenix6
import commands2


class MotorSubsystem(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.phoenixmotor = phoenix6.hardware.TalonFX(1)
        self.controller = wpilib.XboxController

    def go_up(self):
        self.phoenixmotor.set(0.4)

    def go_down(self):
        self.phoenixmotor.set(-0.4)

    def stop(self):
        self.motor.set(0)

    def is_stopped(self):
        motor_speed = self.motor.get()
        if motor_speed == 0:
            return True 
        else:
            return False