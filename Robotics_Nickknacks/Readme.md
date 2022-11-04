# ROS setup
General steps to set up a ROS project <br/>
Create the workspace and source folder with command mkdir -p ws_name/src <br/>
Go in src and type command catkin_init_workspace <br/>
In folder ws_name type command catkin_make <br/>
Go in src and type catkin_create_pkg pakage_name rospy std_msgs (other dependencies)<br/>
Go back in ws_name again and type catkin_make <br/>
Navigate to src/package_name/src/ and create the talker and subscriber <br/>
In package_name create the launch folder and inside that create the launch file <br/>
To run a ros project in ws_name type catkin_make first then source devel/setup.bash and then roslaunch <name_of_package> <name_of_launch_file>
