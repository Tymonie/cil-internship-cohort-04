# cil-internship-cohort-04
# CIL 018

# Question 2. What is the NS IP addresses for Google, Facebook and Tesla? 
NS stands for ‘nameserver,’ and the nameserver record indicates which DNS server is authoritative for that domain (i.e. which server contains the actual DNS records).

NS IP addresses for Google Public DNS

via IPv4 8.8.8.8 8.8.4.4
via IPv6 2001:4860:4860::8888 2001:4860:4860::8844
google.com IPv4: 216.58.208.110 IPv6: 2a00:1450:400e:80e::200e
facebook.com IPv4: 157.240.201.35 IPv6: 2a03:2880:f145:82:face:b00c:0:25de
tesla.com 184.50.204.169 184.30.18.203


# Question 2. Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetwork with no address left over.”#### 1. 10.10.10.0#### 2. 192.168.0.0#### 3. 172.168.1.0

---
## For 10.10.10.0
This is an IPv4 class A (range of 0-127)
To get the value of the subnet mask we can use a simple table
Subnet | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |---| --- | --- | --- | --- | --- | --- | --- | --- | --- |Host | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |subnet mask | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
so for 4 subnetwork the value is 10 i.e __10.10.10.0/10__subnet mask = __255.192.0.0__ (in binary format)
And each subnetwork is within range of __64__
S/NO| Network ID | Broadcast ID | Useable IP Address---| --- | --- | --- 1 | 10.0.0.0/10 | 10.63.255.255/10 | 10.0.0.1/10 - 10.63.255.254/102 | 10.64.0.0/10 | 10.127.255.255/10 | 10.64.0.1/10 - 10.127.255.254/103 | 10.128.0.0/10 | 10.191.255.255/10 | 10.128.0.1/10 - 10.191.255.254/104 | 10.192.0.0/10 | 10.255.255.255/10 | 10.192.0.1/10 - 10.255.255.254/10
---
## For 192.168.0.0
This is an IPv4 class C (range of 192-223)
To get the value of the subnet mask we can use a simple table
Subnet | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |---| --- | --- | --- | --- | --- | --- | --- | --- | --- |Host | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |subnet mask | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |
so for 4 subnetwork the value is 26 i.e __192.168.0.0/26__subnet mask = __255.255.255.192__ (in binary format)
And each subnetwork is within range of __64__
S/NO| Network ID | Broadcast ID | Useable IP Address---| --- | --- | --- 1 | 192.168.0.0/10 | 192.168.0.63/10 | 192.168.0.1/10 - 192.168.0.62/102 | 192.168.0.64/10 | 192.168.0.127/10 | 192.168.0.65/10 - 192.168.0.126/103 | 192.168.0.128/10 | 192.168.0.191/10 | 192.168.0.129/10 - 192.168.0.190/104 | 192.168.0.192/10 | 192.168.0.255/10 | 192.168.0.193/10 - 192.168.0.254/10
---
## For 172.168.1.0
This is an IPv4 class B (range of 128-191)
To get the value of the subnet mask we can use a simple table
Subnet | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 |---| --- | --- | --- | --- | --- | --- | --- | --- | --- |Host | 256 | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |subnet mask | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
so for 4 subnetwork the value is 18 i.e __172.168.1.0/18__subnet mask = __255.255.192.0__ (in binary format)
And each subnetwork is within range of __64__
S/NO| Network ID | Broadcast ID | Useable IP Address---| --- | --- | --- 1 | 172.168.0.0/10 | 172.168.63.255/10 | 172.168.0.1/10 - 172.168.63.254/102 | 172.168.64.0/10 | 172.168.127.255/10 | 172.168.64.1/10 - 172.168.127.254/103 | 172.168.128.0/10 | 172.168.191.255/10 | 172.168.128.1/10 - 172.168.191.254/104 | 172.168.192.0/10 | 172.168.255.255/10 | 172.168.192.1/10 - 172.168.255.254/10
