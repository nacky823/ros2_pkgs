import rclpy
from rclpy.node import Node
from person_msgs.msg import Person #使う型を変更

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10) #変更
n = 0
def cb():
    global n
    msg = Person()         #受信するデータの型を変更
    msg.name = "田中修辞"  #msgファイルに書いた「name」
    msg.age = n            #msgファイルに書いた「age」
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
