#!/bin/sh
echo "what is you destination IP address?"
read IPDes
echo "what is your destination port number?"
read portDes
echo "what is your source IP number?"
read IPSource
echo "what is your source port number?"
read portSource
echo "which interface do you want to use?"
read interface
echo "what is your source MAC address?"
read MAcSource
echo "what is your destination MAC address?"
read MAcDes

file="/home/ubunto-virtual-machin/hello/info.txt"
echo $IPDes > $file
echo $portDes >> $file
echo $IPSource >> $file
echo $portSource>> $file
echo $interface>> $file
echo $MAcSource>> $file
echo $MAcDes>> $file

cat $file
# cat <<EOF >/home/ubunto-virtual-machin/hello/info.txt

# second line
# third line
# EOF


