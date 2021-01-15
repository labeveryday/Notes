# Linux notes

To verify your linux download

```bash
echo "hash *file_name.iso" | shasum -a 1 --check
```

How to create a directory and change to it

```bash
mkdir mytest && cd mytest
```

## Configure Linux Dev Environment

Install Linux utilities

```bash
sudo apt update
sudo apt upgrade

sudo apt install curl

sudo apt install libssl-dev

sudo apt install build-essential

sudo apt install git

sudo apt-get install python3-venv

sudo apt install nodejs

sudo apt install npm

sudo apt install snapd

sudo snap install atom --classic

sudo snap install postman

sudo snap install ngrok

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt update

sudo apt install docker-ce

sudo usermod -aG docker $USER
```

### Linux Commands

| Commands                                          | Description                                               |
| -------------                                     | :-------------:                                           |
| pwd                                               | Print current working directory
| ls                                                | List contents of working directory (ls -l test.txt will show file permissions and file/group owner)|
| man <command>                                     | View manual pages (how-to) to learn how to use a given command and it’s flags (man ls)
| Sudo                                              | Super User Privileges root 
| $                                                 | Signifies that the user does not have root privileges
| #                                                 | Root privilege
| Apt & apt-get                                     | Debian family of distributions to install packages (sudo apt-get install traceroute)
| Touch                                             | Creates an empty new file without automatically overwriting existing files with the same name. It also updates the files timestamps. (touch config.txt)|
| Mkdir                                             | Make a new directory
| Mkdir -p                                          | Make all required sub-directories in the path
| Rm                                                | Removes a file
| Rm -r                                             | Removes an entire directory and its contents
| Rmdir                                             | Removes an entire directory
| Cp                                                | Copy a file (cp file1 file2)
| Mv                                                | Move/rename a file (mv file2 file3) (mv test.txt home/cisco/nexus home/cisco/Testing)
| More                                              | Similar to using Cisco CLI-space bar takes down a full screen length (% in bottom left)
| Less                                              | “less is more” Scroll up and down with arrow keys
| Cat                                               | Streams the file top to bottom (cat router1.txt)
| Head                                              | Shows first 10 lines
| Tail                                              | Shows last 10 lines of a file
| Diff                                              | View the difference between two files (diff -u test.cfg test_new.cfg)
| Chmod                                             | Change file permissions (use ls -l to view file permissions and the chmod u+x test.txt to add execute)
| Top                                               | Displays real time processor utilization
| Htop                                              | Displays real time processor utilization in an easier to read format
| Ps                                                | Displays real time processor utilization in an easier to read format (more arguments available)
| Ps aux                                            | Displays an exhaustive list of all running processes by all users
| cat /etc/*release                                 | Determine your version of linux
| Echo "this is a test" >>test.txt                  | Create a new file with text inside
| ping                                              | Test connectivity between two nodes. In Linux, ping will run continuously unless manually stopped. Supports options such as on Cisco CLI (hint: man pages). |  
| traceroute                                        | Displays the layer 3 hops taken to reach a destination
| ifconfig                                          | Displays interface information of all interfaces
| ifconfigeth1                                      | Displays interface information of a specific interface
| Ip addr                                           | Assign or delete an IP address to a specific interface
| Ip route                                          | Add a route to the local system (sudo ip rroute add 172.16.10.0/24 via 192.168.200.50 dev eth1)
| Ip route list                                     | Primary methon for viewing and modifying the routing table.
| Route                                             | Another command to view and modify the routing table
| Arp                                               | View local system Arp table. Set a static arp entry. 
| Netstat                                           | Display local computer’s connection information, routing table information
| Netstat -r                                        | Displaying only local routing table (same as the route command)
| Netstat -i                                        | Displays very useful interface statistics
| Dig                                               | Display DNS information (dig www.cisco.com)
| Host                                              | Resolve a hostname to an IP address or learn DNS info (host www.cisco.com)
| Resolv.conf                                       | DNS information is stored here. (/etc/resolv.conf)
| ifup/ifdown                                       | Used to enable or disable an interface
| Ssh                                               | Securely log into remote systems (ssh -l duan 192.168.2.1 -p 2000)
| /etc/network/interfaces                           | Interface and route information is stored here. (less /etc/network/interfaces)
| Nano                                              | Opens text editor (nano /etc/network/interfaces)
| Sudo service networking restart                   | Networking service must be restated after making changes to the network configuration. |
| Nc -zv <ip> port#                                 | Check is a device is listening on a specific port
| Cd /var/log/loghosts                              | Check logs on a device
| Traceroute -I x.x.x.x                             | Return hops when running traceroute (Use ICMP ECHO for probes)
| Nmap -sP x.x.x.x/24                               | Find available ip addresses in a subnet. 
| tcpdump -w tcaptest.cap -i bond0 port 443         |
| Tcpdump -i eth0 tcp port 80 -w /var/temp/test.pcap|
| fping -l 10.1.1.1 10.1.1.2                        |
