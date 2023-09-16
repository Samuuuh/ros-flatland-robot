# Intelligent Robotics - 2D Reactive Robot on Flatland
This projects implements a 2D reactive robot that wanders around an environment until an end position is reached. The project was built using Robot Operating System (ROS) and the Flatland Package.

## Installation 
This assignment was done with [ROS Noetic Ninjemys](http://wiki.ros.org/noetic). 
Ubuntu 20.04 LTS (Focal Fossa) was used since this is the one that natively supports ROS Noetic.

1. Download and install Ubuntu 20.04 (Focal).
2. After Ubuntu 20.03 is installed, is necessary to install ROS. For ROS installation, this [installation guide](http://wiki.ros.org/noetic/Installation/Ubuntu) was followed. 

3. Our project depends on [Flatland](https://flatland-simulator.readthedocs.io/en/latest/) which is a performance centric 2D robot simulator started at Avidbots Corp.
It's necessary to install this extra dependencie for the package to run:
```
$ sudo apt-get update
$ sudo apt-get install liblua5.1-0-dev
```

4. After everything is installed, it's necessary to setup the folders in order to run the project. Let's start by creating the necessary folders. The folder `flatland_ws` will be the root for this project.
```
$ mkdir flatland_ws
$ cd flatland_ws
$ mkdir src
$ cd src
```

5. In the folder `flatland_ws/src/` you will put the [Flatland Repository](https://github.com/avidbots/flatland). You also need to copy the `assignment_one` folder inside this repository under the folder `flatland_ws/src`.  
  ```
  $ git clone https://github.com/avidbots/flatland
  ```
  
6. After the previous step, you should have the following folders: `flatland_ws/src/flatland` and `flatland_ws/src/assignment_one/`. Now it is necessary to allow the python code to be executable.
```
chmod +x assignment_one/robot_movement.py assignment_one/robot_movement.py assignment_one/run.py assignment_one/world.py
cd ..
```
7. Build the project on the root and activate the environment
```
catkin_make
source devel/setup.bash
```

8. After the last step, the project is ready to run.

## Usage
Inside the `assignment_one`folder, the user should run the following command:
```
python run.py [target_x] [target_y]
```

The user can also choose wether the robot should stop or not at the tip of the letter "Ç" by passing a target value as follows
```
python run.py -1 -17
```

## Folder Structure
This repository was the following folder structure:
```
.              
├── assignment_one                 # ROS Project Files
│   ├── launch              
│   │   └── assignment_one.launch  # File responsible to initialize the program
│   ├── models                     # Models of the map and robot
│   │   ├── world.yaml
│   │   └── ...
│   ├── robot_movement.py          # Manage sensor information and gives actions to the robot
│   ├── run.py                     # Inits the program
│   ├── world.py                   # Generate the map and the initial position of the robot
│   └── ..                         # Packages necessary to run the ROS Project
└── README.md
```

## Contributors
| Name             | Number    | E-Mail             |
| ---------------- | --------- | ------------------ |
| Diogo Fernandes  | 201806250 | up201806250@edu.fe.up.pt |
| Hugo Guimarães   | 201806490 | up201806490@edu.fe.up.pt |
| Iohan Sardinha   | 201801011 | up201801011@edu.fe.up.pt |
