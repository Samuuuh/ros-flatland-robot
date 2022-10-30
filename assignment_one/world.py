#!/bin/python3
from random import randint
from math import pi

class GenerateMap:
  def __init__(self):
    self.map_num = randint(1,7)
    self.pos = self.get_robot_pos()
    
  def get_robot_pos(self):
    if self.map_num == 2:
      return [randint(-11,2), randint(-5,5), randint(-90,90)/360*2*pi ] 
    else:
      return [randint(-5,5),randint(-5,5), randint(90,270)/360*2*pi ] 

  def get_world(self):
    return f"""
    properties:
      velocity_iterations: 10
      position_iterations: 10

    layers:
      - name: \"layer_1\"
        map: \"map.yaml\"
        color: [0, 0, 1, 1]

    models:
      - name: reactive1
        pose: [{self.pos[0]}, {self.pos[1]}, {self.pos[2]}]
        model: \"reactive.model.yaml\" 
    """

  def get_map(self):
    return f"""
    image: {self.map_num}.png
    resolution: 0.150000
    origin: [-25, -20, 0.000000]
    negate: 1                     
    occupied_thresh: 0.804
    free_thresh: 0.196
    """
