#!/bin/python3
import os
from threading import Thread
from time import sleep

from world import GenerateMap
from robot_movement import main

if __name__ == "__main__":
    environment = GenerateMap()
    with open("models/map.yaml", "w") as map_file:
        map_file.write(environment.get_map())

    with open("models/world.yaml", "w") as world_file:
        world_file.write(environment.get_world())

    os.system("cd ../.. && roslaunch assignment_one assignment_one.launch")
