import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
import tf2_ros as tf2
from pyquaternion import Quaternion
from geometry_msgs.msg import Twist, TransformStamped, Quaternion as GeometryQuaternion
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu  # IMU 메시지 임포트
from math import sin, cos
from tf2_ros import TransformBroadcaster
from nav_msgs.msg import Odometry
from std_msgs.msg import Float32MultiArray


class OdomPublisher(Node):

    def __init__(self):
        super().__init__('odom_from_cmd_vel')
        
        self.x = 0.0
        self.y = 0.0
        self.th = 0.0

        self.vx = 0.0
        self.vth = 0.0

        self.last_time = self.get_clock().now()
        # self.tf_broadcaster = TransformBroadcaster(self)

        self.utm_sub = self.create_subscription(
            Float32MultiArray, 
            "/utm_coordinates", 
            self.utm_callback, 
            QoSProfile(depth=10))

        self.prev_utm = None

        # IMU 데이터를 구독
        self.imu_sub = self.create_subscription(
            Imu,
            "/imu",
            self.imu_callback,
            QoSProfile(depth=10))

        self.odom_pub = self.create_publisher(
            Odometry, 
            "odom", 
            QoSProfile(depth=50))
        
        timer_period = 0.01  # 20Hz
        self.timer = self.create_timer(timer_period, self.update)
        
    def cmd_vel_callback(self, data):
        self.vx = data.linear.x
        self.vth = data.angular.z

    def quat_to_yaw(self, quaternion):
        """Convert a quaternion to yaw angle."""
        import math
        s = 2.0 * (quaternion.w * quaternion.z + quaternion.x * quaternion.y)
        c = 1.0 - 2.0 * (quaternion.y**2 + quaternion.z**2)
        yaw = math.atan2(s, c)
        return yaw

    def imu_callback(self, data):  # IMU 콜백 함수
        quat = Quaternion(data.orientation.w, data.orientation.x, data.orientation.y, data.orientation.z)
        self.th = self.quat_to_yaw(quat)

    def utm_callback(self, data):
        if self.prev_utm:
            delta_x = data.data[0] - self.prev_utm.data[0]
            delta_y = data.data[1]- self.prev_utm.data[1]
            
            # Update robot's pose based on the change in UTM coordinates
            self.x += delta_x
            self.y += delta_y
            
        self.prev_utm = data

    def update(self):
        current_time = self.get_clock().now()
        quat = Quaternion(axis=[0, 0, 1], angle=self.th)
        odom_quat_msg = GeometryQuaternion()
        odom_quat_msg.x = quat.x
        odom_quat_msg.y = quat.y
        odom_quat_msg.z = quat.z
        odom_quat_msg.w = quat.w

        print(self.x, self.y)
        #  Create and publish odometry message
        odom = Odometry()
        odom.header.stamp = current_time.to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"
        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation = odom_quat_msg
        odom.twist.twist.linear.x = self.vx
        odom.twist.twist.angular.z = self.vth
        self.odom_pub.publish(odom)

        self.last_time = current_time


def main(args=None):
    rclpy.init(args=args)
    odom_publisher = OdomPublisher()
    rclpy.spin(odom_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
