from random import randint
from math import pi

MAP_NUM = randint(1,7)

if MAP_NUM == 2:
  POS = [randint(-11,2), randint(-5,5) ,randint(-90,90)/360*2*pi ] 
else:
  POS = [randint(-5,5),randint(-5,5), randint(90,270)/360*2*pi ] 

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

MAP = f"""
image: {MAP_NUM}.png                             # begin with "/" for absolute, otherwise relative w.r.t this file
resolution: 0.150000
origin: [-25, -20, 0.000000]
negate: 1                                  # NOT used
occupied_thresh: 0.804
free_thresh: 0.196                         # NOT used
"""