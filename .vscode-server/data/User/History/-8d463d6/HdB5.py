#!/usr/bin/env python
import rospy
from morai_msgs.srv import WoowaDillyEventCmdSrv
from morai_msgs.msg import DillyCmd, WoowaDillyStatus
from std_msgs.msg import Int32MultiArray

class Fsm():
    def __init__(self) -> None:
        rospy.init_node('fsm', anonymous=True)
        rospy.Subscriber('/WoowaDillyStatus', WoowaDillyStatus, self.dilly_status)
        rospy.wait_for_service('/WoowaDillyEventCmd')
        self.service_client = rospy.ServiceProxy('/WoowaDillyEventCmd', WoowaDillyEventCmdSrv)
        self.state_pub = rospy.Publisher('/state', Int32MultiArray, queue_size=10)
        self.destination_plan = [(0,5,True),(5,1,True),(1,15,False), (15,11,False)]  # From To pickup
        self.curr_order = 0

        self.dilly_st = ()
        self.from_point = 0
        self.to_point = 0
        self.pickup = False
        self.success = False
        try:
            while not rospy.is_shutdown():
                print("FROM POINTS: ", self.from_point)
                print("TO POINTS: ", self.to_point)
                print("STATUS: ", self.pickup, self.success)

                self.from_point = self.destination_plan[self.curr_order][0]
                self.to_point = self.destination_plan[self.curr_order][1]
                self.pickup = self.destination_plan[self.curr_order][2]

                my_array = Int32MultiArray()
                my_array.data = [self.from_point, self.to_point, self.pickup]
                self.state_pub.publish(my_array)

                if self.from_point < 10:
                    self.event(self.pickup , self.from_point)
                    if self.from_point in self.dilly_st:
                        self.curr_order += 1
                else:
                    self.event(self.pickup ,self.from_point - 10)
                    if not self.from_point - 10 in self.dilly_st:
                        self.curr_order += 1


        except Exception as e:
            rospy.logerr(f"Failed to read and publish the path: {e}")
    
    def dilly_status(self, msg):
        self.dilly_st = msg.deliveryItem

    def event(self, pickup, itemIdx):
        request = DillyCmd()
        request.isPickup = pickup
        request.deliveryItemIndex = itemIdx
        response = self.service_client(request)
        print(pickup, itemIdx)

    
if __name__ == '__main__':
    a = Fsm()
