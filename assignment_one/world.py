from random import randint
from math import pi

POS= [randint(-5,5),randint(-5,5), randint(90,270)/360*2*pi]
WORLD = f"""properties:
  velocity_iterations: 10
  position_iterations: 10
  
layers:
  - name: \"layer_1\"
    map: \"map.yaml\"
    color: [0, 0, 1, 1]
    
models:
  - name: reactive1
    pose: [{POS[0]}, {POS[1]}, {POS[2]}]
    model: \"reactive.model.yaml\" 
"""