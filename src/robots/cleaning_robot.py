from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: str, cleaning_tool: str):
        """
        Initializes a cleaning robot

        Parameters:
        --
        :param name (str): The name of the robot.
        :param battery_level (int): The initial battery level of the robot (0 to 100).
        :param status (string): The status of the robot ('idle', 'working', 'charging').
        :param cleaning_tool: str (e.g., vacuum, mop)
        """
        Robot.__init__(self,name, battery_level, status)
        self.cleaning_tool = cleaning_tool
    
    def work(self):
        """
        Cleans the room, uses 20% battery
        """
        if self.battery_level < 20:
            print("Battery too low to clean, charge it")
        else:
            print("Cleaning...")
            self.set_status = "working"
            self.battery_level -= 20
    
    def set_tool(self, cleaning_tool: str) -> None:
        """
        Sets the cleaning tool
        
        Parameter:
        --
        :param cleaning_tool: str (e.g., vacuum, mop)
        """
        self.cleaning_tool = cleaning_tool
    
    def get_tool(self) -> str:
        """
        Returns the cleaning tool (String)
        """
        return self.cleaning_tool
