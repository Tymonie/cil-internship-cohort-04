##### **Name: Jeffrey Esedo**
##### **Candidate No: 053**

## **cil-internship-cohort-04**
#### **Model One**
###### Internship Week - 2


#### ***Task 1:*** 
##### Describe any layered process you are familiar with similar to the OSI model

## TCP/IP
Mostly curated from [GeeksforGeeks] (https://www.geeksforgeeks.org/similarities-between-tcp-ip-model-and-osi-model/)

### **What is the TCP/IP model?**

Transmission Control Protocol/Internet Protocol, or TCP/IP model for short, TCP/IP consists of four layers, each of which has certain functions. These layers are the layers through which data flows when it is transferred from one place on earth to another with the help of a network, basically starting at the lowest layer and ending at the highest layer before reaching its destination. The TCP/IP model has the following layers. 

It was designed and developed by the U.S. Department of Defense (DoD) in the 1960s and is based on standard protocols. The TCP/IP model is a simplified version of the OSI model.

image.png

#### •	__APPLICATION / 1st LAYER__
Describing from the user/sender to the receiver perspective, it is responsible for node-to-node communication and controls user-interface specifications, it is the layer that interacts with an application program. Some of the protocols present in this layer are: HTTP, HTTPS, FTP, TFTP, Telnet, SSH, SMTP, SNMP, NTP, DNS, DHCP, NFS, X Window, LPD etc.

#### •	__HOST TO HOST/ TRANSPORT / 2nd LAYER__
This layer is similar to the transport layer of the OSI model. It is responsible for end-to-end communication and error-free delivery of data; it determines how much data should be sent where and at what speed. This layer also protects upper layer applications from data complexity. The two main protocols present in this layer are; Transmission Control Protocol (TCP) and User Datagram Protocol (UDP)

#### •	__INTERNET / 3rd LAYER__
It defines the protocol responsible for the logical transmission of data throughout the network, the internet layer is to send packets from any network or any computer until they reach their destination, regardless of their route. The main protocols residing at this layer are; IP (Internet Protocol), ICMP (Internet Control Message Protocol), ARP (Address Resolution Protocol). 

#### •	__NETWORK INTERFANCE / 4TH LAYER__
This layer is equivalent to the combination of the data link layer and the physical layer of the OSI model. Taking care of hardware addressing, the protocols present in this layer enable the physical transmission of data.
And vice versa from a receiver to a senders perspective.

#### *Differences Between OSI and TCP/IP models*
Compared to the OSI model, the TCP/IP model follows a horizontal approach, unlike OSI model TCP/IP uses both Session and Presentation layer in the Application layer itself. Transport layer does not provide assurance delivery of packets, the Network layer provided just the connectionless services, and protocols cannot be easily replaced in the TCP/IP model. The OSI model is made up of 7 layers.



#### ***Task 2:***

##### - What are the NS IP addresses for Google, Facebook and Tesla?
##### - Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetwork with no address left over. 
    * 10.10.10.0
    * 192.168.0.0
    * 172.168.1.0

**Google**
*Name:*    www.google.com
*Addresses:*2c0f:fb50:4003:801::2004
            216.58.223.228

**Facebook**
*Name:*       star-mini.C10R.facebook.com
*Addresses:*  2a03:2880:f138:83:face:b00c:0:25de
              102.132.101.35
*Aliases:*    www.facebook.com

**Tesla**
*Name:*     e1792.dscx.akamaiedge.net
*Address:*  104.75.172.54
*Aliases:*  www.tesla.com 
            www.tesla.com.edgekey.net


Subnet = 4
Default Subnet mask = 255.255.255.000
4 Subnet Binary = 11111111. 11111111. 11111111. 11000000
Number of bit/ CIDR - 26
11 – Subnetwork ID, 000000 – 6 Host ID
4 Subnet Decimal = 255.255.255.196
Formula for subnetting – 2^n: 2 ^ 6 = 64 
Formula for number of Hosts per Subnet – 2^n – 2: 64 – 2 = 62

|10.10.10.0 – 63 / 26|192.168.0.0 – 63 / 26|172.168.1.0 – 63 /26|
|10.10.10.64 – 127 / 26|192.168.0.64 – 127 / 26|172.168.1.64 – 127 /26|
|10.10.10.128 – 191 / 26|192.168.0.128 – 191 / 26|172.168.1.128 – 191 /26|
|10.10.10.192 – 255 / 26|192.168.0.192 – 255 / 26|172.168.1.192 – 255 /26|
