import rclpy
from rclpy.node import Node
from person_msgs.srv import Query #使う型を変更

def cb(request, response):
    if request.name == "田中修辞":
        response.age = 22
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb) #サービスの作成
rclpy.spin(node)
