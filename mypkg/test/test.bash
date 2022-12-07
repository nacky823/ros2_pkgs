#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"  # このシェルスクリプトに引数があれば、それをホームとする。

cd $dir/robosys/ros2
colcon build
source $dir/.bashrc

ros2 launch mypkg talk_listen.launch.py
