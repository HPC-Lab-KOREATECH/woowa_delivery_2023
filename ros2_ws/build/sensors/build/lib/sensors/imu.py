import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanFrameChanger(Node):

    def __init__(self):
        super().__init__('scan_frame_changer')
        self.new_frame_id = "laser"

        self.subscription = self.create_subscription(
            LaserScan, 
            '/scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.publisher = self.create_publisher(LaserScan, '/laser', 10)

    def listener_callback(self, msg):
        changed_msg = msg
        changed_msg.header.frame_id = self.new_frame_id
        self.publisher.publish(changed_msg)

def main(args=None):
    rclpy.init(args=args)

    scan_frame_changer = ScanFrameChanger()

    rclpy.spin(scan_frame_changer)

    scan_frame_changer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
