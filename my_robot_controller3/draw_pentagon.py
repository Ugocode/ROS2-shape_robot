
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import math

class DrawRectangleNode(Node):
    def __init__(self):
        super().__init__("Draw_pentagon")
        self.pose_subscriber_ =self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10) #listener / subscriber 
        self.cmd_vel_publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) #talker / publisher
        self.get_logger().info("Pentagon drawing started")
        self.counter = 0
        self.target_degree = (math.pi / 180) * 72

    # Now how the code will operate:
    def turn(self, cmd: Twist):
        cmd.angular.z = self.target_degree - 0.015
        cmd.linear.x = 0.0
        self.cmd_vel_publisher_.publish(cmd)
        time.sleep(2)

    def go(self, cmd: Twist, times):
        cmd.angular.z = 0.0
        cmd.linear.x = float(times)
        self.cmd_vel_publisher_.publish(cmd)
        time.sleep(3)

    def stop(self, cmd:Twist):
        cmd.angular.z = 0.0
        cmd.linear.x = 0.0
        self.cmd_vel_publisher_.publish(cmd)
        time.sleep(0.5)

    def pose_callback(self, pose: Pose):
        cmd = Twist()

        if self.counter == 0: 
            self.go(cmd, 2)
            self.stop(cmd)
            self.turn(cmd)
            self.stop(cmd)
            self.counter += 1
        else:
            self.go(cmd, 2)
            self.stop(cmd)
            self.turn(cmd)
            self.stop(cmd)
            self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = DrawRectangleNode()
    rclpy.spin(node)
    rclpy.shutdown()
    