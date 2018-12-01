#!/usr/bin/env python
from turtlebot_ctrl.srv import TurtleBotControl
from geometry_msgs.msg import Point
from std_msgs.msg import Bool
import rospy

class TurtlebotControlClient:
	def __init__(self):
		rospy.init_node("turtlebot_control_client")

		rospy.wait_for_service("turtlebot_control")
		self.turtlebot_control_service = rospy.ServiceProxy("turtlebot_control",TurtleBotControl)

	def run(self):
		key = ""
		while key != 's':
			key = raw_input("WASD:")
			req = Point()
			return_ground_truth = Bool()
			return_ground_truth.data = True

			if key == 'q':
				req.x = -1
				req.y = 1
			elif key == 'w':
				req.y = 1
			elif key == 'e':
				req.x = 1
				req.y = 1
			elif key == 'a':
				req.x = -1
			elif key == 'd':
				req.x = 1
			elif key == 'z':
				req.x = -1
				req.y = -1
			elif key == 'x':
				req.y = -1
			elif key == 'c':
				req.x = 1
				req.y = -1

			print(req)
			print(self.turtlebot_control_service(req,return_ground_truth))

		rospy.spin()

if __name__ == "__main__":
	try:
		turtlebot_control_client = TurtlebotControlClient()
		turtlebot_control_client.run()
	except rospy.ROSInterruptException:
		pass