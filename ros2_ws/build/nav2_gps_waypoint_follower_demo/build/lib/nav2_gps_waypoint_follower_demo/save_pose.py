import rclpy
from rclpy.node import Node
import json
from nav_msgs.msg import Odometry

class SaveWaypointsNode(Node):
    def __init__(self):
        super().__init__('save_waypoints_node')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        self.timer = self.create_timer(5.0, self.timer_callback) # 5초마다 timer_callback 호출
        self.latest_pose = None # 최신 pose를 저장하는 변수
        self.waypoints = []

        # 파일이 이미 존재하면 기존 waypoints를 로드합니다.
        try:
            with open('waypoints.json', 'r') as file:
                self.waypoints = json.load(file)
        except FileNotFoundError:
            pass

    def listener_callback(self, msg):
        self.latest_pose = {
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

    def timer_callback(self):
        if self.latest_pose:
            self.waypoints.append(self.latest_pose)
            with open('waypoints.json', 'w') as json_file:
                json.dump(self.waypoints, json_file)
                self.get_logger().info("Saved waypoint to waypoints.json")
            self.latest_pose = None

def main(args=None):
    rclpy.init(args=args)
    node = SaveWaypointsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
