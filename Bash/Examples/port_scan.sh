#! /bin/bash

# This script is designed to find hosts with MySQL installed
# Send the screen output to /dev/null so that it disappears
# Then send the output to a file name MySQLscan

nmap -sT 192.168.1.0/24 -p 3306 > /dev/null -oG MySQLscan 

cat MSQLscan | grep open > MySQLscan2

cat MySQLscan2
