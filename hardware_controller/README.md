# The hardware_controller Package

## Overview

The hardware_controller package is the hardware interface and controller package. Contains the central logic of the system.

**Keywords:** controller, interface, hub

### License

**Author: Dionesius Agung<br />
Maintainer: Dionesius Agung, 13516043@std.stei.itb.ac.id**

The hardware_controller package has been tested under [ROS] Kinetic and Ubuntu 16.04. This is a specific-purpose code, expect it not to work for your needs unless any proper changes to your specifications is made.


## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [rosserial] (ROS serialized messages wrapper)
- [rosserial_python] (Python-based implementation of rosserial)

		sudo apt-get install ros-kinetic-rosserial ros-kinetic-rosserial-python


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd <your_workspace>/src
	git clone https://gitlab.informatika.org/if3111-2019-waterbase/ros-packages/hardware_controller.git
	cd ../
	catkin_make


## Usage

Run the main node with

	roslaunch hardware_controller hardware_interface.launch


## Nodes

### controller_node.py

Acts as the data hub/gateway from sensors and API server. Processes the data and send commands based on those data.

#### Subscribed Topics

* **`/data/api_cmd`** ([std_msgs/String])

	A message indicating that something has requested for a particular route.

* **`/data/sensors`** ([arduino_msgs/SensorsMsg](https://gitlab.informatika.org/if3111-2019-waterbase/ros-packages/arduino_msgs))

	The measurement results from a group of sensors.


#### Published Topics

* **`/cmd/eff`** ([arduino_msgs/EffectorsMsg](https://gitlab.informatika.org/if3111-2019-waterbase/ros-packages/arduino_msgs))

	Command for each effectors or actuators.


[ROS]: http://www.ros.org
[rosserial]: http://wiki.ros.org/rosserial
[rosserial_python]: http://wiki.ros.org/rosserial_python?distro=kinetic
[std_msgs/String]: http://docs.ros.org/api/std_msgs/html/msg/String.html