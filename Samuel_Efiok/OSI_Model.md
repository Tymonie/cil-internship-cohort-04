## What is the NS IP addresses for Google, Facebook and Tesla?
## Answer:
NS stands for ‘nameserver,’ and the nameserver record indicates which DNS server is 
authoritative for that domain (i.e., which server contains the actual DNS records). 
Basically, NS records tell the Internet where to go to find out a domain's IP address. A 
domain often has multiple NS records which can indicate primary and secondary 
nameservers for that domain. Without properly configured NS records, users will be 
unable to load a website or application.

You can ping a domain name and find the corresponding IP address.
NSlookup is a network tool for querying a DNS (Domain Name System) to obtain a 
domain name, an IP address, or for any other DNS record for a website.
- Google 
    - Server: google.com
     - Addresses: 2c0f:fb50:4003:801::200e, 
 216.58.223.206
- Facebook 
     - Server: facebook.com
     - Addresses: 2a03:2880:f138:83:face:b00c:0:25de, 
 102.132.101.35
- Tesla 
    - Server: tesla.com
     - Addresses: 23.201.26.71, 
 184.30.18.203, 
 96.16.108.43, 
 23.9.66.10, 
 104.119.104.74, 
 184.85.228.70, 
 184.50.204.169


# Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetworks with no address left over?
    10.10.10.0
    192.168.0.0
    172.168.1.0




## What is RFC 1918 IPv4  address range ? 

RFC 1918 address range describes the use of IP address space deemed private by internet assigned number authority IANA and this means that this Private address space is available for use by any organisation and is guaranteed to be not routable in the public Internet. 

Note: Network classes can be easily identified by the number of their first octet 

## E.g

- Class A - first octet value 
0-126

- Class B - first octet value
128-191

- Class C - first octet value
192-233

- Class D - first octet value 
224 - 239

- Class E - first octet value 
240 - 255

##### ( Back to the question! )

The 10.10.10.0 is a class A subnet IP address which first oct range from 0-126 and has a default subnet of 255.0.0.0 i.e 8bit allocated to the network and 24bit to the host, again we know this by quickly checking the first octet of the address and comparing it with the network classes.

192.168.0.0 is a class C  subnet IP address which the first octet ranges from 192- 233 and has a default subnet of 
255.255.255.0

172.168.1.0  is a type B subnet IP address which the  first octet value ranges from 128-191and has a default subnet of 255.255.0.0






# Describe any layered process you are familiar with similar to the OSI model.
## TCP/IP model: 
Just Like the OSI model, the TCP/IP model is layered and is used in the same fashion but 
with fewer layers. As the modern Internet and most communications use the Internet 
Protocol (IP), the TCP/IP model is technically more in line with modern network 
implementations. Its layers include;
1. Application Layer
2. Transport Layer
3. Internet (Network) Layer
4. Data link Layer

#### Application Layer: 
This is the highest layer in the TCP/IP model and is related to the session, 
presentation and application layers of the OSI model. Define the protocols and 
standards that application requires to connect to the network. It provides services for 
network application with the help of a protocol to perform user activities. The 
application layer of the TCP/IP model is used to handle all process-to-process 
communication functions; these functions are carried out by multiple different layers 
when referencing the OSI model. There are a number of different functions which are 
carried out by this layer, including session establishment, maintenance and 
termination, character code translations, data conversion, compression and 
encryption, remote access, network management and electronic messaging to name 
a few. Common protocols include Named Pipes, HTTP, SMTP and many others. All 
network applications are dependent on application layer protocol to function. It forms 
the basis for various network services. E.g. Telnet, NetBIOS, MIME, TLS, SSL, FTP,
HTTP/HTTPS, SMTP, DHCP, DNS etc.
#### Transport Layer: 
The Transport layer is the next layer and is typically related directly 
with its namesake layer in the OSI model. Transport layer builds on the network layer 
in order to provide data transport from a process on a source system machine to a process on a destination system. It is hosted using single or multiple networks, and 
also maintains the quality of service functions.
It determines how much data should be sent where and at what rate. This layer builds 
on the message which are received from the application layer. It helps ensure that data 
units are delivered error-free and in sequence.
Transport layer helps you to control the reliability of a link through flow control, error 
control, and segmentation or de-segmentation.
The transport layer also offers an acknowledgment of the successful data transmission 
and sends the next data in case no errors occurred. TCP is the best-known example of 
the transport layer.
#### Internet Layer
The internet layer is a second layer of the TCP/IP model. It is also known as a network 
layer. The main function of this layer is to send the packets from any network, and any 
computer to their destination irrespective of the route they take.
The Internet layer offers the functional and procedural method for transferring 
variable length of data sequences from one node to another with the help of various 
networks.
It uses IP protocol. Data unit in network layer is called packet and data packets contain 
the IP address of sender/ receiver.
Layer-management protocols that belong to the network layer are:
- Routing protocols
- Multicast group management
- Network-layer address assignment.
#### Data link layer
This is also referred to in some texts as the network interface layer. The link layer 
combines the physical and data link layer functions into a single layer.
It is the lowest layer of the TCP/IP model Define standards and protocols for data 
transmission and physical connectivity. Data link controls how data is sent and received. It uses MAC (Media Access Control) to form a frame. This is the layer where 
switching resides. Data from application layer has been segmented by transport layer 
and placed into packets by network layer and framed by data link layer to a sequence 
of 0 and 1 (Binary). This layer is responsible for the transmission of the data between 
two devices on the same network.

The data link layer includes frame physical network functions like modulation, line 
coding and bit synchronization, frame synchronization and error detection, and LLC 
and MAC sublayer functions. Common protocols include the Address Resolution 
Protocol (ARP), Neighbor Discovery Protocol (NDP), IEEE 802.3 and IEEE 802.11.
