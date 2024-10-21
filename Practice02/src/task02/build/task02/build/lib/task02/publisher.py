import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')

        self.declare_parameter('topic_name', '/default_topic')
        self.declare_parameter('text', 'Hello, ROS2!')

        self.topic_name = self.get_parameter('topic_name').get_parameter_value().string_value
        self.text = self.get_parameter('text').get_parameter_value().string_value

        self.publisher_ = self.create_publisher(String, self.topic_name, 10)

        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.get_logger().info(self.topic_name)

    def timer_callback(self):
        msg = String()
        msg.data = self.text
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
