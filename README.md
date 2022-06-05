# Robotics - Assignment

# Problem statement
Write a ROS node (Python or C++) for a differential drive robot in an unknown environment to implement the following trajectory:
![image](./images/robot_path.png)

### Note:
• Assume that the robot is using navigation stack of ROS. <br/>
• The robot must begin and end its path in the given orientations.<br/>
• Use move_base package to achieve the above solution.<br/>
• Configure all the parameters of move_base required for path planning and obstacle avoidance.<br/>
• Send us the written node along with the configuration files for move_base.<br/>
• Also attach a short report (not more than one page) briefly explaining your approach towards the solution.

# Solution
## Turtlebot following a trajectory in empty world in gazebo environment
### Terminal 1
`cd catkin_ws`<br/>
`roslaunch simple_navigation_goals gazebo_navigation_rviz.launch`<br/>
### Terminal 2
`rosrun simple_navigation_goals move_base_wps.py`

|Output of Turtlebot navigating the given waypoints in empty world|
|:------------:|
|![Output video](./images/turtlebot_wps.gif)|
|[Youtube Link](https://youtu.be/ysVizCS7czk)|

## Plotting trajectory (x-y coordinates) taken by the turtlebot (given waypoints) and  yaw angles 
- Recording rosbags of amcl_pose topic <br/>
`rosbag record /amcl_pose`
- Saving rosbag as a text file <br/>
`rostopic echo -p -b 2022-06-05-10-13-46.bag /amcl_pose > pose.txt`<br/>
- Plotting <br/>
`python3 plot_wps.py`<br/>
![x-y](./images/trajectory_taken.png)
![yaw](./images/yaw.png)

# Installation
### Installing ROS Navigation stack
`sudo apt-get install ros-melodic-navigation`

### Running chefbot
`mkdir ~/catkin_ws/src` <br/>
`catkin_create_pkg chefbot_description catkin xacro`<br/>
`catkin build`<br/>
`sudo apt update`<br/>
`sudo apt install ros-melodic-joint-state-publisher-gui`<br/>
 `roslaunch chefbot_description view_robot.launch`<br/>
 ![chefbot](./images/chefbot.png)


### Running chefbot in gazebo
`sudo apt install ros-melodic-depthimage-to-laserscan -y`
follow the [tutorial](https://automaticaddison.com/how-to-launch-the-turtlebot3-simulation-with-ros/) for turtlebot3 installation in ros melodic 

### move base
`sudo apt update`
`sudo apt install ros-move-base-msgs`

### Slam gmapping 
Create a 2D occupancy grid map from the laser scan data and the mobile robot pose.

