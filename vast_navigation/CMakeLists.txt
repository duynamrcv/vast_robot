cmake_minimum_required(VERSION 3.0.2)
project(vast_navigation)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  roscpp
  rospy
  tf
  tf2
)


catkin_package()

include_directories( ${catkin_INCLUDE_DIRS})

catkin_install_python(PROGRAMS
  scripts/test_nav.py
  scripts/plot_data.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)