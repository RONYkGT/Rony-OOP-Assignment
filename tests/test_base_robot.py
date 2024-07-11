import unittest
import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import modules from 'src'
from robots.base_robot import Robot

class TestRobot(unittest.TestCase):
    
    def setUp(self):
        # Initialize objects that will be used in the tests
        self.robot = Robot(name="TestRobot", battery_level=50, status="idle")
    
    def test_initialization(self):
        # Test that the robot is initialized correctly
        self.assertEqual(self.robot.name, "TestRobot")
        self.assertEqual(self.robot.battery_level, 50)
        self.assertEqual(self.robot.status, "idle")
    
    def test_charge_method(self):
        # Test that the charge method works correctly
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
    
    def test_invalid_battery_level(self):
        # Test invalid battery levels
        robot_with_high_battery = Robot(name="HighBatteryRobot", battery_level=120, status="idle")
        self.assertEqual(robot_with_high_battery.battery_level, 100)
        
        robot_with_negative_battery = Robot(name="NegativeBatteryRobot", battery_level=-20, status="idle")
        self.assertEqual(robot_with_negative_battery.battery_level, 0)
    
    def test_report_status_method(self):
        # Test that the report_status method works correctly
        expected_output = "Robot TestRobot is idle with 50% battery"
        self.assertEqual(self.robot.report_status(), expected_output)

if __name__ == '__main__':
    unittest.main()
