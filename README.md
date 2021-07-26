# VAST Robot

## vast_gazebo
This package is the robot simulator using Gazebo in Rviz
```
$ roslaunch vast_gazebo robot.launch
```
### Subscriber topics
```/cmd_vel```: geometry_msgs/Twist <br>
### Publisher topics
```/odom```: nav_msgs/Odometry <br>
```/scan```: sensor_msgs/Scan <br>

## vast_teleop
This package is the keyboard teleop controller to control robot
```
$ roslaunch vast_teleop teleop
```
### Publisher topics
```/cmd_vel```: geometry_msgs/Twist <br>

## vast_gmapping
This package is the SLAM package for robot using Gmapping method
```
$ roslaunch vast_gmapping slam_mapping.launch
```
When the mapping is finish, you will save the map
```
$ rosrun map_server map_saver -f mymap
```

## vast_navigation
```
$ roslaunch vast_navigation vast_navigation.launch
```