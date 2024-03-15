from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():
    return LaunchDescription([
        # Include the velodyne nodes
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(["/opt/ros/galactic/share/velodyne/launch/velodyne-all-nodes-VLP16-launch.py"])
        ),
        
        # Run the ros1_bridge
        # Node(
        #     package='ros1_bridge',
        #     executable='dynamic_bridge',
        #     name='dynamic_bridge'
        # ),
        
        # Launch the sam_bot display nodes
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(["/root/ros2_ws/src/sam_bot_description/launch/display.launch.py"])
        ),

        # Run the tf for sensors
        Node(
            package='sensors',
            executable='tf',
            name='tf'
        ),
        
        # Launch the nav2_gps_waypoint_follower with rviz
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(['/root/ros2_ws/src/nav2_gps_waypoint_follower_demo/launch/gps_waypoint_follower.launch.py']),
            launch_arguments={'use_rviz': 'True'}.items()
        ),

        # # Run the woowa_planning
        # Node(
        #     package='nav2_gps_waypoint_follower_demo',
        #     executable='woowa_planning',
        #     name='woowa_planning'
        # ),
    ])
