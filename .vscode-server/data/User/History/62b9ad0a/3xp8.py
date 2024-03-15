import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped, Pose
from nav_msgs.msg import Odometry
import json
import math
from std_msgs.msg import Int32MultiArray
from nav2_msgs.action import NavigateToPose
import time  # 시간을 추적하기 위해 time 모듈을 추가

class WaypointClient(Node):

    def __init__(self):
        super().__init__('waypoint_client')
        self._action_client = ActionClient(self, FollowWaypoints, '/follow_waypoints')
        self.subscription = self.create_subscription(Odometry, '/odometry/global', self.odom_callback, 10)
        self.array_subscription = self.create_subscription(Int32MultiArray, '/state', self.array_callback, 10)  # 새로운 구독을 추가합니다.
        self.client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        self.current_pose = Pose()
        self.previous_pose = self.current_pose
        self.waypoints = []
        self.previous_array_data = None  # 값을 저장하기 위한 변수를 추가합니다.
        self.filename = "/root/ros2_ws/src/nav2_gps_waypoint_follower_demo/map/0_5.json"
        self.current_index = 0
        self.last_movement_time = time.time()  # 마지막으로 로봇이 움직였을 때의 시간을 저장하는 변수
        self.current_goal = None
        self.map_set = False
    def array_callback(self, msg):
        # Int32MultiArray 값이 변경되었는지 확인합니다.
        if self.previous_array_data != msg.data:
            self.map_set = True
            self.previous_array_data = msg.data  # 현재 값을 저장합니다.
            self.filename = f"/root/ros2_ws/src/nav2_gps_waypoint_follower_demo/map/{msg.data[0]}_{msg.data[1]}.json"
            self.load_waypoints_from_file(self.filename)
            self.current_index = self.find_nearest_waypoint()
            self.send_waypoint()
            print("HEEELLLLO")

    def odom_callback(self, msg):
        self.current_pose = msg.pose.pose
        distance_moved = self.calculate_distance(self.current_pose, self.previous_pose)
        if self.map_set:
            print(distance_moved)
            if distance_moved > 10.0:  # 순간 이동
                self.current_index = self.find_nearest_waypoint()
                print("순간이동")
            elif distance_moved == 0.0:  # if no movement recovery
                print("RECOVERY!!!!!!!!")
                self.send_waypoint()

            self.previous_pose = self.current_pose
            distance = 99999999
            if len(self.waypoints) != 0:
                distance = self.calculate_distance(self.current_pose, self.waypoints[self.current_index].pose)
            if distance < 2:
                if self.current_index != len(self.waypoints) -1 :
                    self.current_index += 1
                    self.send_waypoint()

    def load_waypoints_from_file(self, filename='0_5.json'):
        print(filename,"<+++++")
        with open(filename, 'r') as f:
            waypoints_data = json.load(f)
            for data in waypoints_data:
                waypoint = PoseStamped()
                waypoint.header.frame_id = "map"
                waypoint.pose.position.x = data['position']['x']
                waypoint.pose.position.y = data['position']['y']
                waypoint.pose.position.z = data['position']['z']
                waypoint.pose.orientation.x = data['orientation']['x']
                waypoint.pose.orientation.y = data['orientation']['y']
                waypoint.pose.orientation.z = data['orientation']['z']
                waypoint.pose.orientation.w = data['orientation']['w']
                self.waypoints.append(waypoint)

    def calculate_distance(self, pose1, pose2):
        return math.sqrt((pose1.position.x - pose2.position.x)**2 + (pose1.position.y - pose2.position.y)**2)

    def find_nearest_waypoint(self):
        min_distance = float('inf')
        nearest_index = 0
        for index, waypoint in enumerate(self.waypoints):
            distance = self.calculate_distance(self.current_pose, waypoint.pose)
            if distance < min_distance:
                min_distance = distance
                nearest_index = index
        return nearest_index

    def send_waypoint(self):
        goal_msg = NavigateToPose.Goal()
        waypoint = self.waypoints[self.current_index]
        goal_msg.pose.header.frame_id = 'map'  # 'map'은 일반적인 frame_id입니다. 실제 환경에 맞게 수정하세요.
        goal_msg.pose.pose.position.x = waypoint.pose.position.x  # 예시 위치
        goal_msg.pose.pose.position.y = waypoint.pose.position.y
        goal_msg.pose.pose.position.z = waypoint.pose.position.z
        goal_msg.pose.pose.orientation.w = waypoint.pose.orientation.w  # Quaternions의 기본 회전
        goal_msg.pose.pose.orientation.z = waypoint.pose.orientation.z  # Quaternions의 기본 회전
        goal_msg.pose.pose.orientation.x = waypoint.pose.orientation.x  # Quaternions의 기본 회전
        goal_msg.pose.pose.orientation.y = waypoint.pose.orientation.y  # Quaternions의 기본 회전
        self.current_goal = goal_msg
        print(1)
        self.client.send_goal_async(goal_msg)
        print(2)

def main(args=None):
    rclpy.init(args=args)
    waypoint_client = WaypointClient()
    rclpy.spin(waypoint_client)
    waypoint_client.destroy_node()
    rclpy.shutdown()