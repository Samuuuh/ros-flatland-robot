# Intelligent Robotics

## Assignment One
This assignment was done with ROS Noetic. Thus, Ubuntu Focal as used since this is the oen that provide compatability with this this version
Setup Operating System + ROS:
Download and install Ubuntu 20.04 (Focal).
For ROS installation, this guide was followed: http://wiki.ros.org/noetic/Installation/Ubuntu

Before getting started, it's necessary to install other dependencies necessaries for flatland:
```
sudo apt-get update
sudo apt-get install liblua5.1-0-dev
```

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
