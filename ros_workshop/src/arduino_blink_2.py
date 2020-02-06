#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('blink',Int32, queue_size=10)
    rospy.init_node('arduino_blink', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    n = rospy.get_param("num",10)
    n=n-1
    while not rospy.is_shutdown():
        if n>=0:
            data = 1
            pub.publish(data)
            rate.sleep()
            data = 0
            pub.publish(data)
            rate.sleep()
            n=n-1;


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
