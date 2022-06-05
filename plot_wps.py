import numpy as np
import matplotlib.pyplot as plt
import math

def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)
        #roll_x = math.degrees(roll_x) # in degrees

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)
        #pitch_y = math.degrees(pitch_y) # in degrees

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)
        yaw_z = math.degrees(yaw_z) # in degrees

        return roll_x, pitch_y, yaw_z # in radians

pos = ((0.0, 0.0, 0.0), (0.4, 1.0, 0.0), (1.6, 1.0, 0.0), (2.0,0.0,0.0))

x_coord = []
y_coord = []


for r in range(len(pos)):
    x_coord.append(pos[r][0])
    y_coord.append(pos[r][1])

plt.plot(x_coord, y_coord, 'xk', linestyle='-', label= 'given x-y way point coordinates')


time_stamp, pos_x, pos_y, pos_z = [], [], [], []
pos_or_x, pos_or_y, pos_or_z, pos_or_w = [], [], [], []
pos_roll_x, pos_pitch_y, pos_yaw_z = [], [], []


with open ('pose.txt') as f:
    next(f)
    for line in f:
        line_split = line.split(",")


        for word in range(len(line_split)):
            if word == 0:
                time_stamp.append(float(line_split[word]))
            if word == 4:
                pos_x.append(float(line_split[word]))
            if word == 5:
                pos_y.append(float(line_split[word]))
            if word == 6:
                pos_z.append(float(line_split[word]))
            if word == 7:
                pos_or_x.append(float(line_split[word]))
            if word == 8:
                pos_or_y.append(float(line_split[word]))
            if word == 9:
                pos_or_z.append(float(line_split[word]))
            if word == 10:
                pos_or_w.append(float(line_split[word]))
        #print ("\n")
f.close()

plt.plot(pos_x, pos_y, marker = '.', markersize=0.1, color = "red", label='trajectory taken by turtlebot3')
plt.title("x-y plot grid and rover trajectory")
plt.legend()
plt.show()

for m in range (len(pos_or_x)):
    roll_x, pitch_y, yaw_z = euler_from_quaternion(pos_or_x[m], pos_or_y[m], pos_or_z[m], pos_or_w[m])
    print ("roll_x, pitch_y, yaw_z:", roll_x, pitch_y, yaw_z)
    pos_roll_x.append(roll_x)
    pos_pitch_y.append(pitch_y)
    pos_yaw_z.append(yaw_z)

plt.plot(time_stamp, pos_yaw_z, marker = 'x', color = 'r')
plt.title("time vs pos_yaw_z(degrees)")
plt.show()
