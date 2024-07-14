from .cleaning_robot import CleaningRobot
from .cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name: str, battery_level: int, status: str, cleaning_tool: str, cooking_skill: str) -> None:
        CleaningRobot.__init__(self, name, battery_level, status, cleaning_tool)
        CookingRobot.__init__(self, name, battery_level, status, cooking_skill)

    def multi_task(self) -> None:
        print(f"{self.name} starting multi-tasking:")
        self.work() # This will clean because CleaningRobot is its first parent.
        CookingRobot.work(self)
