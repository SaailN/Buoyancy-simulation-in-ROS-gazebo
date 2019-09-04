#!/usr/bin/env python 
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
 
def talker():
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
   
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10000) # 10hz
    i=0
   
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        position1 = math.sin(i)
        rospy.loginfo(position1)
        pub1.publish(position1)
        
        i=i+0.05
        
        
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass