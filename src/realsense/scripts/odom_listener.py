#! /usr/bin/env python
import rospy
from matplotlib import pyplot as plt
from geometry_msgs.msg import PoseWithCovarianceStamped

# Global list to store positions
positions = []

def callback(data):
    _position = data.pose.pose.position
    print(str(_position) + "\n")
    # Append position data to the global list
    positions.append((_position.x, _position.y))

def update_plot():
    if positions:  # Check if there are new positions to plot
        x, y = zip(*positions)  # Unzip the positions into x and y coordinates
        plt.scatter(x, y)  # Plot the new positions
        plt.draw()  # Redraw the plot with the new data
        plt.pause(0.05)  # Pause to update the plot

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/rtabmap/localization_pose", PoseWithCovarianceStamped, callback)
    plt.ion()  # Enable interactive mode
    plt.show()

    # Main loop
    while not rospy.is_shutdown():
        update_plot()
        rospy.sleep(0.1)  # Sleep to yield control to ROS

if __name__ == '__main__':
    listener()

