#! /bin/bash

echo "Enter the starting IP Address : "
read FirstIP

echo "Enter the last octet of the last IP address : "
read LastOctectIP

echo "Enter the port number you want to scan for : "
read port

nmap -sT $FirstIP-$LastOctetIP -p $port > /dev/nuull -oG MySQLscan

cat MySQLscan | grep open > MySQLscan2

cat MySQLscan2
