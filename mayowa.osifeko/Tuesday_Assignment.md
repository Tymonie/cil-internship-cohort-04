TuesSubnetting day Assignment

# What is the NS IP addresses for Google, Facebook, and Tesla?
### Via https://www.gaijin.at/en/tools/nameserver-lookup#result 
1. Google: 142.250.185.68
2. Facebook: 157.240.20.35
3. Tesla: 23.203.40.54

# Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnets with no address left over.
 - 10.10.10.0
 - 192.168.0.0
 - 172.168.1.0
 
 IP address breakdown to 4 subnets

10.10.10.0 – class A – default subnet/subnet mask of 255.0.0.0/8
10.10.10.0 will have a subnet mask of /10 (255.192.0.0) for 4 subnets therefore subnet address will be:

|**Network ID**|**Host ID Range**|**Broadcast ID**|
|:-----------|:------------:|:-----------:|
|10.0.0.0|	10.0.0.1 – 10.63.255.254|10.63.255.255|
|10.64.0.0|10.64.0.1– 10.127.255.254|10.127.255.255|
|10.128.0.0|10.128.0.1–10.191.255.254|10.191.255.255|
|10.192.0.0|10.192.0.1–10.255.255.254|10.255.255.255|

172.168.1.0 – class B – default subnet/subnet mask of 255.255.0.0/16
 
172.168.1.0 will have a subnet mask of /18 (255.225.192.0) for 4 subnets therefore subnet address will be:

|**Network ID**|**Host ID Range**|**Broadcast ID**|
|:-----------|:------------:|:-----------:|
|172.168.0.0|172.168.0.1–172.168.63.254|172.168.63.255|
|172.168.64.0|172.168.64.1–172.168.127.254|172.168.127.255|
|172.168.128.0|172.168.128.1–172.168.191.254|	172.168.191.255|
|172.168.192.0|172.168.192.1–172.168.255.254|	172.168.255.255

192.168.0.0	will have a subnet mask of /26 (255.225.225.192) for 4 subnets therefore subnet address will be:

|**Network ID**|**Host ID Range**|**Broadcast ID**|
|:-----------|:------------:|:-----------:|
|192.168.0.0|192.168.0.1–192.168.0.62|192.168.0.63|
|192.168.0.64|192.168.0.65–192.168.0.126|192.168.0.127|
|192.168.0.128|192.168.0.129–192.168.0.190|192.168.0.191|
|192.168.0.192|192.168.0.193–192.168.0.254|192.168.0.255|