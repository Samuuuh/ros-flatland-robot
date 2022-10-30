import os
from world import WORLD, MAP
from robot_movement import main
from threading import Thread
from time import sleep

with open("models/map.yaml", "w") as map_file:
    map_file.write(MAP)

with open("models/world.yaml", "w") as world_file:
    world_file.write(WORLD)

os.system("cd ../.. && roslaunch assignment_one assignment_one.launch")