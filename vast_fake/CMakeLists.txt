cmake_minimum_required(VERSION 3.0.2)
project(vast_fake)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  nav_msgs
  roscpp
  rospy
  sensor_msgs
  tf
  tf2
)

# catkin_python_setup()

catkin_package()
include_directories( ${catkin_INCLUDE_DIRS} )

add_executable(vast_fake_node src/vast_fake_node.cpp)
target_link_libraries(vast_fake_node ${catkin_LIBRARIES})

add_executable(odom_path_node src/odom_path_node.cpp)
target_link_libraries(odom_path_node ${catkin_LIBRARIES})