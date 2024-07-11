from abc import abstractmethod

class Robot:

    def __init__(self, name: str, battery_level: int, status: str = "idle"):
        """
        Initialize a new Robot instance.

        Parameters:
        ------
        :param name (str): The name of the robot.
        :param battery_level (int): The initial battery level of the robot (0 to 100).
        :param status (string): The status of the robot ('idle', 'working', 'charging').
        """
        self.name = name

        if battery_level > 100:
            self.battery_level = 100
        elif battery_level < 0:
            self.battery_level = 0
        else:
            self.battery_level = battery_level
        
        if status == "idle" or status == "working" or status == "charging" :
            self.status = status
        else:
            self.status = "idle"
    
    def charge(self) -> None:
        """
        Charge the robot's battery to 100.
        """
        self.battery_level = 100
        self.set_status = "charging"
    
    @abstractmethod
    def work(self) -> None:
        pass

    def report_status(self) -> str:
        """
        Report the robot's status.
        """
        return f"Robot {self.name} is {self.status} with {self.battery_level}% battery"
        
    def set_name(self, name: str) -> None:
        """
        Set the robot's name

        Parameters:
        -------
        Name (str): Set the name
        """
        self.name = name
    
    def set_status(self, status: str) -> None:
        """
        Set the robot's status
        
        Parameteres:
        --
        status (str): Set the status (idle, working, charging) default value: idle
        """
        if status == "idle" or status == "working" or status == "charging" :
            self.status = status
        else:
            self.status = "idle"
    
    def get_name(self) -> str:
        """
        Get the robot's name.

        Returns:
        -------
        str: The robot's name.
        """
        return self.name

    def get_status(self) -> str:
        """
        Get the robot's status.

        Returns:
        -------
        str: The robot's status.
        """
        return self.status


    

    

        
