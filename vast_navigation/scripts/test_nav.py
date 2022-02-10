import matplotlib.pyplot as plt
import numpy as np
import math

import rospy
from nav_msgs.msg import Odometry
from nav_msgs.msg import Path
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, PoseStamped

draw_robot = []

odom = Odometry()
def odom_callback(data):
    global odom
    odom = data

path = Path()
draw_path = []

def path_callback(data):
    global path
    global draw_path
    path = data

    if draw_path == []:
        for pose in path.poses:
            px = pose.pose.position.x
            py = pose.pose.position.y
            pq = quaternion2Yaw(pose.pose.orientation)
            draw_path.append([px,py,pq])

def quaternion2Yaw(orientation):
    q0 = orientation.x
    q1 = orientation.y
    q2 = orientation.z
    q3 = orientation.w

    yaw = math.atan2(2.0*(q2*q3 + q0*q1), 1.0 - 2.0*(q1*q1 + q2*q2))
    return yaw

def test_nav():
    rospy.init_node("test_nav", anonymous=True)

    # Subscriber
    rospy.Subscriber("/odom", Odometry, odom_callback)
    rospy.Subscriber("/move_base/GlobalPlanner/plan", Path, path_callback)
    
    rate = 50
    r = rospy.Rate(rate)

    while not rospy.is_shutdown():
        px = odom.pose.pose.position.x
        py = odom.pose.pose.position.y
        pq = quaternion2Yaw(odom.pose.pose.orientation)
        draw_robot.append([px,py,pq])
        print([px,py,pq])

        rospy.on_shutdown(store_data)
        r.sleep()

def store_data():
    print("[INFO] Save data!!!")
    import scipy.io
    scipy.io.savemat('/home/duynam/vast_ws/src/vast_robot/vast_navigation/data/robot.mat', dict(ans=draw_robot))
    scipy.io.savemat('/home/duynam/vast_ws/src/vast_robot/vast_navigation/data/ref.mat', dict(ans=draw_path))


if __name__ == '__main__':    
    try:
        test_nav()
    except rospy.ROSInterruptException:
        pass