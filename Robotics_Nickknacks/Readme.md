# ROS setup
General steps to set up a ROS project
Create the workspace and source folder with command mkdir -p ws_name/src
Go in src and type command catkin_init_workspace
In folder ws_name type command catkin_make
Go in src and type catkin_create_pkg pakage_name rospy std_msgs (other dependencies)
Go back in ws_name again and type catkin_make
Navigate to src/package_name/src/ and create the talker and subscriber
In package_name create the launch folder and inside that create the launch file 8)To run a ros project in ws_name type catkin_make first then source devel/setup.bash and then roslaunch <name_of_package> <name_of_launch_file>
