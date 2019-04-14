#!/usr/bin/env python
import rospy
#Importing Twist message: Used to send velocity to Turtlesim
from geometry_msgs.msg import Twist
#Handling command line arguments
import sys
#Function to move turtle: Linear and angular velocities are arguments
def move_turtle(lin_vel,ang_vel):
    rospy.init_node('move_turtle', anonymous=False)
        #The /turtle1/cmd_vel is the topic in which we have to send Twist messages
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz
        #Creating Twist message instance
    vel = Twist()
    while not rospy.is_shutdown():
#Adding linear and angular velocity to the message
                vel.linear.x = lin_vel
                vel.linear.y = 0
                vel.linear.z = 0
                vel.angular.x = 0
                vel.angular.y = 0
                vel.angular.z = ang_vel
                rospy.loginfo("Linear Vel = %f: Angular Vel = %f",lin_vel,ang_vel)
                #Publishing Twist message
                pub.publish(vel)
                rate.sleep()
if __name__ == '__main__':
    try:
#Providing linear and angular velocity through command line
        move_turtle(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass
