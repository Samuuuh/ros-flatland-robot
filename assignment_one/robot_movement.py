#!/bin/python3
import rospy
import math

from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan, NavSatFix

def distance(p,q):
    return math.sqrt(((p[0] - q[0])**2) + ((p[1] - q[1])**2))

class Turtle:
    def __init__(self, target=None):
        self.target = target
        self.arrived = False

        # Init RosPy
        rospy.init_node('flatland_server', anonymous=True)
        
        # Publishers
        self.pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	    # Subscribers
        self.sub_lase_sensor = rospy.Subscriber('/scan', LaserScan, self.callback_laser, tcp_nodelay=True)
        self.sub_gps = rospy.Subscriber('/gps', NavSatFix, self.callback_gps)

    def callback_gps(self, data):
        lat = int(round(data.latitude ,7)*10**7)/100
        lng = int(round(data.longitude,7)*10**7)/100
        if self.target is None or self.arrived: return
        TARGET_DISTANCE = 1
        
        d = distance([lng, lat], self.target)
        print("x = ",lng, ", y = ",lat, ", d = ", d)

        self.arrived = d < TARGET_DISTANCE


    def callback_laser(self, data):
        max_distance = 2
        min_distance = 2
        
        right_laser_range = data.ranges[0] 
        middle_laser_range = data.ranges[1]
        left_laser_range = data.ranges[2]
        
        #print(f"right: {right_laser_range}")
        #print(f"middle: {middle_laser_range}")
        vel_msg = Twist()
  	
  	# Andar até chegar à parede
        LIN_VEL = 2
        if self.arrived:
            vel_msg.angular.z = 5
        elif not math.isnan(right_laser_range):
            if (middle_laser_range <= 3):
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = 2
            elif right_laser_range > 1:
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = -2
            else:
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = 2
        else:
            if (middle_laser_range > 3):
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = 0
            elif (middle_laser_range <= 3):
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = 2
            else:
                vel_msg.linear.x = LIN_VEL
                vel_msg.angular.z = -2
        
        self.pub_cmd_vel.publish(vel_msg)
  

def main(target = None):
    
    try:
        turtle = Turtle(target)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logwarn(f'Service failed with the exception {e}')

if __name__ == '__main__':
    main()
