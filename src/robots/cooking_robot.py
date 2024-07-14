from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: str, cooking_skill: str):
        """
        Initializes a cooking robot

        Parameters:
        --
        :param name (str): The name of the robot.
        :param battery_level (int): The initial battery level of the robot (0 to 100).
        :param status (string): The status of the robot ('idle', 'working', 'charging').
        :param cooking_skill: str (e.g., beginner, intermediate, expert)
        """
        Robot.__init__(self,name, battery_level, status)
        self.cooking_skill = cooking_skill
    
    def work(self):
        """
        LET HIM COOK, uses 30% battery
        """
        if self.battery_level < 30:
            print("Battery too low to cook, charge it")
        else:
            print("Bro cooked")
            self.set_status = "working"
            self.battery_level -= 30
    
    def set_skill(self, cooking_skill: str) -> None:
        """
        Sets the cooking skill.

        Parameters:
        ---
        :param cooking_skill: str (e.g., beginner, intermediate, expert)
        """
    
    def get_skill(self) -> str:
        """
        Gets the cooking skill.
        Returns string.
        """
        return self.cooking_skill
