# What are the NS IP addresses for Google, Facebook and Tesla?

## Google IP Address
> IPV6: **2a03:2880:f164:81:face:b00c:0:25de**

>IPV4: **102.132.101.35**

<br>

## Facebook IP Address
> IPV6: **2a03:2880:f164:81:face:b00c:0:25de**

>IPV4: **102.132.101.35**

<br>

## Tesla IP Address
> IPV4: **184.85.228.70**

>IPV4: **23.9.66.10**

<br>

# Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetwork with no address left over
- 10.10.10.0; 
- 192.168.0.0; 
- 172.168.1.0

To break the IP addresses, I'll firstly identify the class ID for each IP Address.

<br>

- **10.10.10.0 (Class A ID)**

Subnet | 1 | 2 |  **4**| 8 | 16 | 32 | 64 | 128 | 256 |
---| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Host | 256 | 128 |  **64** | 32 | 16 | 8 | 4 | 2 | 1 |
Subnet mask | 8 | 9 |  **10** | 11 | 12 | 13 | 14 | 15 | 16 |

Since the number of subnetwork required is 4, each subnest will have 64 different host IDs, with /10 subnet mask for each of the subnetwork IDs. 

Since 10.10.10.0 = 255.0.0.0 in binary, the new 4 subnets with the network IDs, usable host ID range and broadcast IDs will be shown in tabular form as; 

No.| Network ID | Host ID Range |  Broadcast ID |
---| --- | --- | --- 
1 | 10.0.0.0/10  |  10.0.0.1/10 - 10.63.255.254/10 | 10.63.255.255/10 |
2 | 10.64.0.0/10 | 10.64.0.1/10 - 10.127.255.254/10 | 10.127.255.255/10 | 
3 | 10.128.0.0/10 | 10.128.0.1/10 - 10.191.255.254/10 |10.191.255.255/10 |
4 | 10.192.0.0/10 | 10.192.0.1/10 - 10.255.255.254/10 | 10.255.255.255/10 | 

<br>

- **192.168.0.0 (Class C ID)**

Subnet | 1 | 2 |  **4**| 8 | 16 | 32 | 64 | 128 | 256 |
---| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Host | 256 | 128 |  **64** | 32 | 16 | 8 | 4 | 2 | 1 |
Subnet mask | 24 | 25 | **26** | 27 | 28 | 29 | 30 | 31 | 32 |

Since the number of subnetwork required is 4, each subnest will have 64 different host IDs, with /26 subnet mask for each of the subnetwork IDs. 

Since 192.168.0.0 = 255.255.225.0 in binary, the new 4 subnets with the network IDs, usable host ID range and broadcast IDs will be shown in tabular form as; 

No.| Network ID | Host ID Range |  Broadcast ID |
---| --- | --- | --- 
1 | 192.168.0.0/26 |  192.168.0.1/26 - 192.168.0.62/26 |192.168.0.63/26 |
2 | 192.168.0.64/26 |  192.168.0.65/26 - 192.168.0.126/26 |192.168.0.127/26 |
3 | 192.168.0.128/26 |192.168.0.129/26 - 192.168.0.190/26 | 192.168.0.191/26 | 
4 | 192.168.0.192/26 | 192.168.0.193/26 - 192.168.0.254/26  | 192.168.0.255/26 | 

<br>

- **172.168.1.0 (Class B ID)**

Subnet | 1 | 2 |  **4**| 8 | 16 | 32 | 64 | 128 | 256 |
---| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Host | 256 | 128 |  **64** | 32 | 16 | 8 | 4 | 2 | 1 |
subnet mask | 16 | 17 | **18** | 19 | 20 | 21 | 22 | 23 | 24 |

Since the number of subnetwork required is 4, each subnest will have 64 different host IDs, with /18 subnet mask for each of the subnetwork IDs. 

Since 172.168.1.0 = 255.255.0.0 in binary, the new 4 subnets with the network IDs, usable host ID range and broadcast IDs will be shown in tabular form as; 

No.| Network ID | Host ID Range |  Broadcast ID |
---| --- | --- | --- 
1 | 172.168.0.0/18 |  172.168.0.1/18 - 172.168.63.254/18 |172.168.63.255/18 |
2 | 172.168.64.0/18 | 172.168.64.1/18 - 172.168.127.254/18 |172.168.127.255/18 |  
3 | 172.168.128.0/18 |  172.168.128.1/18 - 172.168.191.254/18 |172.168.191.255/18 |
4 | 172.168.192.0/18 |  172.168.192.1/18 - 172.168.255.254/18 |172.168.255.255/18 |