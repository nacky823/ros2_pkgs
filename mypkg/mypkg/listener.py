import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

def cb(msg):
    node.get_logger().info("Listen: %s" % msg) #変更

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Person, "person", cb, 10) #変更
rclpy.spin(node)
