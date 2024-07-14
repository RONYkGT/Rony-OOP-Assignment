# main.py
# Code was done with the help of ChatGPT but was edited and well understood by the student.

from robots import *

def create_robot():
    print("\nCreate a New Robot:")
    robot_type = input("Enter robot type (cleaning/cooking/maintenance): ").lower()
    name = input("Enter robot name: ")
    while True:
        user_input = input("Enter battery level (0-100): ")
        try:
            battery_level = int(user_input)
            if 0 <= battery_level <= 100:
                break
            else:
                print("Battery level must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
    status = input("Enter status (idle, working, charging): ")

    if robot_type == "cleaning":
        cleaning_tool = input("Enter cleaning tool (e.g., vacuum): ")
        return CleaningRobot(name, battery_level, status, cleaning_tool)
    elif robot_type == "cooking":
        cooking_skill = input("Enter cooking skill (e.g., beginner/intermediate/expert): ")
        return CookingRobot(name, battery_level, status, cooking_skill)
    elif robot_type == "maintenance":
        cleaning_tool = input("Enter cleaning tool (e.g., vacuum): ")
        cooking_skill = input("Enter cooking skill (e.g., beginner/intermediate/expert): ")
        return MaintenanceRobot(name, battery_level, status, cleaning_tool, cooking_skill)
    else:
        print("Invalid robot type. Please enter 'cleaning', 'cooking', or 'maintenance'.")
        return None

def self_diagnose(robot):
    while True:
        print(f"\nSelf Diagnose for Robot '{robot.name}':")
        print("1. Check Battery Level")
        print("2. Check Status")
        print("3. Full Self Diagnose")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print(Robot.check_battery_level(robot.get_battery_level()))
        elif choice == "2":
            print(Robot.check_status(robot.get_status()))
        elif choice == "3":
            robot.self_diagnose()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid number.")

def manage_robot(robot):
    while True:
        print(f"\nManaging Robot '{robot.name}':")
        print("1. Check Status")
        print("2. Work")
        print("3. Charge")
        print("4. Self Diagnose")
        if isinstance(robot, MaintenanceRobot):
            print("5. Multi-Task")
            print("6. Exit")
        else:
            print("5. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            print(robot.report_status())
        elif choice == "2":
            robot.work()
        elif choice == "3":
            robot.charge()
        elif choice == "4":
            self_diagnose(robot)
        elif choice == "5" and isinstance(robot, MaintenanceRobot):
            robot.multi_task()
        elif choice == "5" or (choice == "6" and isinstance(robot, MaintenanceRobot)):
            break
        else:
            print("Invalid choice. Please enter a valid number.")

def main():
    robots = []
    while True:
        print("\n===== Robot Management Menu =====")
        print("1. Create New Robot")
        print("2. Manage Existing Robot")
        print("3. Exit")

        option = input("Enter your option (1-3): ")
        if option == "1":
            robot = create_robot()
            if robot:
                robots.append(robot)
                print(f"\nRobot '{robot.name}' created successfully.")
        elif option == "2":
            if not robots:
                print("\nNo robots created yet. Please create a robot first.")
                continue
            print("\nSelect Robot to Manage:")
            for idx, robot in enumerate(robots, start=1):
                print(f"{idx}. {robot.name} ({robot.__class__.__name__})")
            selection = int(input("Enter robot number to manage: ")) - 1
            if 0 <= selection < len(robots):
                manage_robot(robots[selection])
            else:
                print("Invalid selection.")
        elif option == "3":
            print("\nExiting Robot Management Menu.")
            break
        else:
            print("Invalid option. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
