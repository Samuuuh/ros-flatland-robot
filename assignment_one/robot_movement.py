#!/bin/python3
import rospy
import math

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Turtle:
    def __init__(self):
        # Init RosPy
        rospy.init_node('flatland_server', anonymous=True)
        
        # Publishers
        self.pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	# Subscribers
        self.sub_lase_sensor = rospy.Subscriber('/scan', LaserScan, self.callback_laser, tcp_nodelay=True)

    def callback_laser(self, data):
        max_distance = 2
        min_distance = 2
        
        right_laser_range = data.ranges[0] 
        middle_laser_range = data.ranges[1]
        left_laser_range = data.ranges[2]
        
        print(f"right: {right_laser_range}")
        print(f"middle: {middle_laser_range}")
        vel_msg = Twist()
  	
  	# Andar até chegar à parede
        if not math.isnan(right_laser_range):
            if (middle_laser_range <= 3):
                vel_msg.linear.x = 2
                vel_msg.angular.z = 2
            elif right_laser_range > 1:
                vel_msg.linear.x = 2
                vel_msg.angular.z = -2
            else:
                vel_msg.linear.x = 2
                vel_msg.angular.z = 2
        else:
            if (middle_laser_range > 3):
                vel_msg.linear.x = 2
                vel_msg.angular.z = 0
            elif (middle_laser_range <= 3):
                vel_msg.linear.x = 2
                vel_msg.angular.z = 2
            else:
                vel_msg.linear.x = 2
                vel_msg.angular.z = -2
                
        self.pub_cmd_vel.publish(vel_msg)
  

if __name__ == '__main__':
    try:
        turtle = Turtle()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logwarn(f'Service failed with the exception {e}')
