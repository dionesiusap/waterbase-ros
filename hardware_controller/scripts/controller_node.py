#!/usr/bin/env python3

import time

import rospy
from rospy import Time
from rospy.timer import TimerEvent

from std_msgs.msg import String
from arduino_msgs.msg import EffectorsMsg, SensorsMsg


class ControllerNode:

    def __init__(self) -> None:
        rospy.init_node('controller_node')
        rospy.on_shutdown(self._shutdown_handler)
        self._frequency = 2

        self._network_data = {
            'ac': 0,
            'light1': False,
            'light2': False,
            'light3': False
        }
        self._sensors_data = {
            'temp': -999,
            'light': -999
        }
        self._effectors_cmd = {
            'ac': 0,
            'light1': False,
            'light2': False,
            'light3': False
        }

        # setup subscribers
        self._network_sub = rospy.Subscriber('/data/api_cmd', String, self._network_cb)
        self._sensors_sub = rospy.Subscriber('/data/sensors', SensorsMsg, self._sensors_cb)

        # setup publishers
        self._arduino_cmd_pub = rospy.Publisher('/cmd/eff', EffectorsMsg, queue_size=1)

        # setup timer
        self._arduino_cmd_pub_timer = rospy.Timer(
                rospy.Duration.from_sec(1.0 / self._frequency), self._control_effectors)


    # message callbacks
    def _network_cb(self, msg: String) -> None:
        if msg.data != 'ac':
            self._network_data[msg.data] = not self._network_data[msg.data]
        else:
            if self._network_data[msg.data] == 0:
                self._network_data[msg.data] = 50
            elif self._network_data[msg.data] == 50:
                self._network_data[msg.data] = 100
            elif self._network_data[msg.data] == 100:
                self._network_data[msg.data] = 200
            elif self._network_data[msg.data] == 200:
                self._network_data[msg.data] = 0
    

    def _sensors_cb(self, msg: SensorsMsg) -> None:
        self._sensors_data['temp'] = msg.temp
        self._sensors_data['light'] = msg.light


    def _control_effectors(self, timer_event: TimerEvent) -> None:
        for key in self._effectors_cmd:
            self._effectors_cmd[key] = self._network_data[key]
        
        if self._sensors_data['light'] < 50:
            for key in self._effectors_cmd:
                if key != 'ac':
                    self._effectors_cmd[key] = True

        self._publish_arduino_cmd()


    def _publish_arduino_cmd(self) -> None:
        msg = EffectorsMsg()
        msg.ac = self._effectors_cmd['ac']
        msg.light1 = self._effectors_cmd['light1']
        msg.light2 = self._effectors_cmd['light2']
        msg.light3 = self._effectors_cmd['light3']
        self._arduino_cmd_pub.publish(msg)
    

    def _shutdown_handler(self) -> None:
        pass


if __name__ == "__main__":
    try:
        node = ControllerNode()
        while not rospy.is_shutdown():
            time.sleep(1)
    except rospy.ROSInterruptException:
        pass