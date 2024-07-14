# Rony-OOP-Assignment

This repository is for the OOP assignment of session 4 where robot classes were created and tested, along with test classes and a main.py console interface to manage these robots.

## Key Points

- ### Robot Classes:
    A base `Robot` class was implemented, with an abstract method `work()` that is inherited into two sub classes, `CleaningRobot` and `CookingRobot`.

- ### Multi-Inheritance:
    `MaintenanceRobot` class was implemented that inherits from both `CleaningRobot` and `CookingRobot` classes, and uses the MRO feature correctly. Along with a `multi_task()` method that combines both classes work features.

- ### MRO:
    Method Resolution Order (MRO) determines the order in which classes are searched when a method is called in an inheritance hierarchy. In Python, MRO searches for the called method in the calling class, then from left to right checks for the method in the inherited parents, and does the same for each parent class recursively. For example, in the `MaintenanceRobot` class, the MRO goes as follows: 
    ```
    MaintenanceRobot -> CleaningRobot -> CookingRobot -> Robot -> Object
    ```
- ### Test Classes:
    Unit tests were used to ensure the robots run properly and as expected in the `tests` directory.
- ### Interactive Terminal Interface:
    `src/main.py` features a terminal interactive menu where user can create and manage robots in a fun way. This script was done with the help of ChatGPT to speed up code writing and focus on the goal of assignment (Object Oriented Programming).

## Usage
- Clone the repository to your system

- Change to the repo directory and build the docker image:
    ```bash
    docker build -t "robots" .
    ```

- Run the docker image:
    ```bash
    docker run -it robots
    ```
