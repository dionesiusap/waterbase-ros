# The network_api Package

## Overview

The network_api package is a simple API server made in Python using [Flask] framework wrapped in ROS node. It is used to receive requests from external clients and publish messages to another ROS node.

**Keywords:** API, Flask, server

### License

**Author: Dionesius Agung<br />
Maintainer: Dionesius Agung, 13516043@std.stei.itb.ac.id**

The network_api package has been tested under [ROS] Kinetic and Ubuntu 16.04. This is a specific-purpose code, expect it not to work for your needs unless any proper changes to your specifications is made.


## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics),
- [Flask] (Python server microframework)

		pip3 install -U Flask


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd <your_workspace>/src
	git clone https://gitlab.informatika.org/if3111-2019-waterbase/ros-packages/network_api.git
	cd ../
	catkin_make


## Usage

Run the main node with

	rosrun network_api network.py

> `roscore` must be running first



## Nodes

### network.py

Runs the API server.

#### Published Topics

* **`/data/api_cmd`** ([std_msgs/String])

	A message indicating that something has requested for a particular route.


[ROS]: http://www.ros.org
[Flask]: http://flask.pocoo.org/
[std_msgs/String]: http://docs.ros.org/api/std_msgs/html/msg/String.html