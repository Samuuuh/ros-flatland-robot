import os
from world import WORLD
from robot_movement import main
from threading import Thread
from time import sleep

def run_flatlantd():
    os.system("cd ../.. && roslaunch assignment_one assignment_one.launch")

with open("models/world.yaml", "w") as world_file:
    world_file.write(WORLD)

Thread(target = run_flatlantd).start()

sleep(5)
main((-3e-05,0))