# The arduino_msgs Package

## Overview

The arduino_msgs package contains the Message Description Language files for messages that are used by Arduino.

**Keywords:** Arduino, message

### License

**Author: Dionesius Agung<br />
Maintainer: Dionesius Agung, 13516043@std.stei.itb.ac.id**


## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [rosserial] (ROS serialized messages wrapper)
- [rosserial_client] (generalized client side source for rosserial)

		sudo apt-get install ros-kinetic-rosserial ros-kinetic-rosserial-client


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd <your_workspace>/src
	git clone https://gitlab.informatika.org/if3111-2019-waterbase/ros-packages/arduino_msgs.git
	cd ../
	catkin_make


#### Generating Message Headers

In order to be used in Arduino program, header files for each message must be generated. Generate the header files and copy them to Arduino libraries folder (Linux default is `~/Arduino/libraries`) using

    cd <your_workspace>
	rosrun rosserial_client make_libraries . arduino_msgs
	cp -R ros_lib ~/Arduino/libraries/


## Messages

### EffectorsMsg
Command message for actuators.

    bool light1
    bool light2
    bool light3
    uint8 ac


### SensorsMsg
Sensor measurement message.

    int8 temp
    int16 light


[ROS]: http://www.ros.org
[rosserial]: http://wiki.ros.org/rosserial
[rosserial_client]: http://wiki.ros.org/rosserial_client?distro=kinetic
[std_msgs/String]: http://docs.ros.org/api/std_msgs/html/msg/String.html