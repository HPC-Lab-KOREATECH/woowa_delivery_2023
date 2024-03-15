import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
import yaml
from ament_index_python.packages import get_package_share_directory
import os
import sys
import time

from nav2_gps_waypoint_follower_demo.utils.gps_utils import latLonYaw2Geopose


class YamlWaypointParser:
    """
    Parse a set of gps waypoints from a yaml file
    """

    def __init__(self, wps_file_path: str) -> None:
        with open(wps_file_path, 'r') as wps_file:
            self.wps_dict = yaml.safe_load(wps_file)

    def get_wps(self):
        """
        Get an array of geographic_msgs/msg/GeoPose objects from the yaml file
        """
        gepose_wps = []
        for wp in self.wps_dict["waypoints"]:
            latitude, longitude, yaw = wp["latitude"], wp["longitude"], wp["yaw"]
            gepose_wps.append(latLonYaw2Geopose(latitude, longitude, yaw))
        return gepose_wps


class GpsWpCommander():
    """
    Class to use nav2 gps waypoint follower to follow a set of waypoints logged in a yaml file
    """

    def __init__(self, wps_file_path):
        self.navigator = BasicNavigator()
        self.wp_parser = YamlWaypointParser(wps_file_path)

    def start_wpf(self):
        """
        Function to start the waypoint following
        """
        # self.navigator.waitUntilNav2Active(localizer='ekf_filter_node_odom')
        wps = self.wp_parser.get_wps()
        print(wps)
        pose_stamped = geometry_msgs.msg.PoseStamped()
    
        # Assign the position (NOTE: This is an oversimplified conversion and not accurate for real-world use cases)
        pose_stamped.pose.position.x = geo_pose.position.latitude
        pose_stamped.pose.position.y = geo_pose.position.longitude
        pose_stamped.pose.position.z = geo_pose.position.altitude
        
        # Assign the orientation
        pose_stamped.pose.orientation = geo_pose.orientation
    
        # Optionally assign a header, e.g.:
        # pose_stamped.header.stamp = rospy.Time.now()
        # pose_stamped.header.frame_id = "some_frame_id"
    
        self.navigator.followWaypoints(wps)
        while (not self.navigator.isTaskComplete()):
            time.sleep(0.1)
        print("wps completed successfully")


def main():
    rclpy.init()

    # allow to pass the waypoints file as an argument
    default_yaml_file_path = os.path.join(get_package_share_directory(
        "nav2_gps_waypoint_follower_demo"), "config", "demo_waypoints.yaml")
    if len(sys.argv) > 1:
        yaml_file_path = sys.argv[1]
    else:
        yaml_file_path = default_yaml_file_path

    gps_wpf = GpsWpCommander(yaml_file_path)
    gps_wpf.start_wpf()


if __name__ == "__main__":
    main()
