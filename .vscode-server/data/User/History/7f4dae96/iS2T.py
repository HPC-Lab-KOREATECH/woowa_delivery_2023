import rclpy
from rclpy.node import Node
import json
from geometry_msgs.msg import PoseWithCovarianceStamped

class SaveWaypointsNode(Node):
    def __init__(self):
        super().__init__('save_waypoints_node')
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            'initialpose',
            self.listener_callback,
            10)
        self.waypoints = []

        # 파일이 이미 존재하면 기존 waypoints를 로드합니다.
        try:
            with open('waypoints.json', 'r') as file:
                self.waypoints = json.load(file)
        except FileNotFoundError:
            pass

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

        self.waypoints.append(pose_data)
        with open('waypoints.json', 'w') as json_file:
            json.dump(self.waypoints, json_file)
            self.get_logger().info("Saved waypoint to waypoints.json")

def main(args=None):
    rclpy.init(args=args)
    node = SaveWaypointsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
