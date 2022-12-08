#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"  # このシェルスクリプトに引数があれば、それをホームとする。

cd $dir/robosys/ros2
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# grep をパイプで改行し、終了ステータスを観察できるようにしている。
cat /tmp/mypkg.log |
grep 'Listen: 10'
