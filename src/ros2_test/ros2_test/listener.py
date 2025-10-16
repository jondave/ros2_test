import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node): # You can also rename the class for clarity
    """
    A subscriber node that listens to the 'topic' topic.
    """
    def __init__(self):
        # CHANGE THIS LINE
        super().__init__('listener')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    # ... rest of the file is the same ...

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()