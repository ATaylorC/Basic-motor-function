import wpilib
import wpimath.controller

import commands2
import commands2.cmd
import commands2.button

from constants import OP, SW
import Subsystem.Phoenix_motor
from Commands.rotate_motor import Lift, Lower, StopMotor





class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The robot's subsystems
        self.hang = Subsystem.Phoenix_motor.MotorSubsystem()

        # The driver's controller
        self.stick = commands2.button.CommandXboxController(OP.joystick_port)

        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        # rotate emojis left when the left bumper is pressed
        self.stick.leftBumper().onTrue(Lift(self.hang))
        self.stick.leftBumper().onFalse(StopMotor(self.hang))
    
        self.stick.rightBumper().onTrue(Lower(self.hang))
        self.stick.rightBumper().onFalse(StopMotor(self.hang))

    def getAutonomousCommand(self):
        return None

        # rotate emojis right when the right bumper is pressed
      