from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, OpaqueFunction
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    def launch_setup(context):
        # Include the velodyne nodes
        yield IncludeLaunchDescription(
            PythonLaunchDescriptionSource("/opt/ros/galactic/share/velodyne/launch/velodyne-all-nodes-VLP16-launch.py"),
            on_exit=launch_sam_bot
        )
        
    def launch_sam_bot(context):
        # Launch the sam_bot display nodes
        yield IncludeLaunchDescription(
            PythonLaunchDescriptionSource("/root/ros2_ws/src/sam_bot_description/launch/display.launch.py"),
            on_exit=launch_tf_for_sensors
        )

    def launch_tf_for_sensors(context):
        # Run the tf for sensors
        yield Node(
            package='sensors',
            executable='tf',
            name='tf',
            on_exit=launch_gps_waypoint_follower
        )

    def launch_gps_waypoint_follower(context):
        # Launch the nav2_gps_waypoint_follower with rviz
        yield IncludeLaunchDescription(
            PythonLaunchDescriptionSource('/root/ros2_ws/src/nav2_gps_waypoint_follower_demo/launch/gps_waypoint_follower.launch.py'),
            launch_arguments={'use_rviz': 'True'}.items(),
            on_exit=run_woowa_planning
        )

    def run_woowa_planning(context):
        # Run the woowa_planning
        yield Node(
            package='nav2_gps_waypoint_follower_demo',
            executable='woowa_planning',
            name='woowa_planning'
        )

    return LaunchDescription([
        OpaqueFunction(function=launch_setup)
    ])
