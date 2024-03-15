import rclpy
from rclpy.node import Node
import json
from geometry_msgs.msg import PoseWithCovarianceStamped

class SaveInitialPoseNode(Node):
    def __init__(self):
        super().__init__('save_initial_pose_node')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'initialpose',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        pose_data = {
            "position": {
                "x": msg.pose.pose.position.x,
                "y": msg.pose.pose.position.y,
                "z": msg.pose.pose.position.z,
            },
            "orientation": {
                "x": msg.pose.pose.orientation.x,
                "y": msg.pose.pose.orientation.y,
                "z": msg.pose.pose.orientation.z,
                "w": msg.pose.pose.orientation.w,
            }
        }

        with open('initial_pose.json', 'w') as json_file:
            json.dump(pose_data, json_file)
            self.get_logger().info("Saved initial pose to initial_pose.json")

def main(args=None):
    rclpy.init(args=args)
    node = SaveInitialPoseNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()