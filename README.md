# Intelligent Robotics

## Assignment One

Steps necessary to run:

1. Setup necessary folders
```
mkdir flatland_ws
cd flatland_ws
mkdir src
cd src
```

2. In the folder flatland_ws/src you will put the folder assignment_one/ and clone flatland repository
```
git clone https://github.com/avidbots/flatland
```
After this step, you should have the following folders: /src/flatland /src/assignment_one/

3. Allow the python code to be executable
```
chmod +x assignment_one/robot_movement.py
cd ..
```

4. On the root (flatland_ws/) run the following commands
```
catkin_make
roslaunch assignment_one assignment_one.launch
```
