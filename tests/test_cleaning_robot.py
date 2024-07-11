import unittest
import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import modules from 'src'
from robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    
    def setUp(self):
        # Initialize objects that will be used in the tests
        self.robot = CleaningRobot(name="CleaningRobot1", battery_level=20, status="idle", cleaning_tool="vacuum")
    
    def test_initialization(self):
        # Test that the robot is initialized correctly
        self.assertEqual(self.robot.name, "CleaningRobot1")
        self.assertEqual(self.robot.battery_level, 20)
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.cleaning_tool, "vacuum")
    
    def test_cleaning_behavior(self):
        # Test that the robot can clean a room and deplete the battery
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 0)  # Battery will be depleted after one session
    
    def test_insufficient_battery(self):
        # Attempt to work with insufficient battery
        self.robot.work()
        self.assertEqual(self.robot.status, "idle")  # Status should remain idle
        self.assertEqual(self.robot.battery_level, 0)  # Battery should not decrease further
    
    def test_report_status_method(self):
        # Test that the report_status() works properly
        expected_output = "Robot CleaningRobot1 is idle with 20% battery"
        self.assertEqual(self.robot.report_status(), expected_output)

if __name__ == '__main__':
    unittest.main()
