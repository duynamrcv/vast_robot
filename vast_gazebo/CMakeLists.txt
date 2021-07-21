cmake_minimum_required(VERSION 3.0.2)
project(vast_gazebo)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})
