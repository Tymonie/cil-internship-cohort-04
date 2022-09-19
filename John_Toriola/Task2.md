# TASK TWO

Original network id :10.10.10.0

|Network ID| Subnet mask| Host ID range| No of usable host| Broadcast ID|
|;---------|:-----------|:-------------|:-----------------|:-----------|
|10.10.10.0 |/26 |10.10.10.1-10.10.10.62|62| 10.10.10.63
|10.10.10.64 |/26 |10.10.10.65-10.10.10.126 |62 | 10.10.10.127
|10.10.10.128 |/26 |10.10.10.65-10.10.10.126 |62 |10.10.10.191
|10.10.10.192 |/26 |10.10.10.193-10.10.10.254 |62 |10.10.10.255

Original network id : 192.168.0.0

|Network ID |Subnet mask |Host ID range |No of usable host |Broadcast ID |
|;---------|:-----------|:-------------|:-----------------|:-----------|
|192.168.0.0 |/26 |192.168.0.1-192.168.0.62 |62 |192.168.0.63
|192.168.0.64 |/26 |192.168.0.1-192.168.0.62 |62 |192.168.0.63
|192.168.0.128 |/26 |192.168.0.129-192.168.0.190 |62 |192.168.0.191
|192.168.0.192 |/26 |192.168.0.193-192.168.0.254 |62 |192.168.0.255

Original network id : 172.168.1.0

|Network ID |Subnet mask |Host ID range |No of usable host |Broadcast ID |
|;---------|:-----------|:-------------|:-----------------|:-----------|
|172.168.1.0 |/26 |172.168.0.1-172.168.0.62 |62 |172.168.1.63
|172.168.1.64 |/26 |172.168.0.65-172.168.0.126 |62 |172.168.1.127
|172.168.1.128 |/26 |172.168.0.129-172.168.0.190 |62 |172.168.1.191
|172.168.1.192 |/26 |172.168.0.193-172.168.0.254 |62 |172.168.1.255

Q. What are the NS IP addresses for Google, Facebook and Tesla?
Breakdown the following RFC 1918 IPv4 address range into
exactly 4 subnets with no address left over.
The ns IP address for Facebook is 102.132.101.35
The ns IP address for Google is 142.250.184.174
The ns IP address for Tesla is 23.201.26.71
10.10.10.0 subnets:
10.10.10.0 /26 subnet mask: 255.255.255.192
10.10.10.64 /26 subnet mask: 255.255.255.192
10.10.10.128 /26 subnet mask: 255.255.255.192
10.10.10.192 /26 subnet mask: 255.255.255.192
192.168.0.0 subnets:
192.168.0.0 /18 subnet mask: 255.255.192.0
192.168.0.64 /18 subnet mask: 255.255.192.0
192.168.0.128 /18 subnet mask: 255.255.192.0
192.168.0.192 /18 subnet mask: 255.255.192.0
172.168.1.0 subnets:
172.168.1.0 /26 subnet mask: 255.255.255.192
172.168.1.64 /26 subnet mask: 255.255.255.192
172.168.1.128 /26 subnet mask: 255.255.255.192
172.168.1.192 /26 subnet mask: 255.255.255.192
REFERENCES
https://www.guru99.com/tcp-ip-model.html
https://www.computernetworkingnotes.com/ccna-study-guide/simil
arities-and-differences-between-osi-and-tcp-ip-model.html
https://www.imperva.com/learn/application-security/osi-model/
