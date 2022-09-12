
 
1.	What is the NS IP addresses for Google, Facebook and Tesla? 

NS stands for ‘nameserver,’ and the nameserver record indicates which DNS server is authoritative for that domain (i.e., which server contains the actual DNS records). Basically, NS records tell the Internet where to go to find out a domain's IP address. 

• Google – 
Server: google.com 
Addresses: 2c0f:fb50:4003:801::200e, 
216.58.223.206 


• Facebook – 
Server: facebook.com 
Addresses: 2a03:2880:f138:83:face:b00c:0:25de, 
102.132.101.35 


• Tesla – 
Server: tesla.com 
Addresses: 23.201.26.71, 
184.30.18.203, 
96.16.108.43, 
23.9.66.10, 
104.119.104.74, 
184.85.228.70, 
184.50.204.169 


2. “Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetworks with no address left over.” 

10.10.10.0 
192.168.0.0 
172.168.1.0 

RFC 1918 describes the use of IP address space deemed private by IANA, the Internet Assigned Numbers Authority. Private address space is available for use by any organization and is guaranteed to be not routable in the public Internet. What this means in practice is that any host machine which is assigned a private address defined by RFC 
1918 cannot be reached "directly" by any other machine not in the hosting organization’s local network. 
RFC 1918 defines the following address ranges as private, 
•	• 10.0.0.0/8 (addresses 10.0.0.0 through 10.255.255.255 inclusive) 
•	• 172.16.0.0/12 (addresses 172.16.0.0 through 172.31.255.255 inclusive) 
•	• 192.168.0.0/16 (addresses 192.168.0.0 through 192.168.255.255 inclusive). The addresses in these ranges are not routable in the Internet and may be freely used by any organization for local purposes only. 

With an IPv4 IP address, there are five classes of available IP ranges: Class A, Class B, Class C, Class D and Class E, while only A, B, and C are commonly used. 
Each class allows for a range of valid IP addresses, shown in the following table: Class 	Address range 	Supports 
Class A 	1.0.0.1 to 126.255.255.254 	Supports 16 million hosts on each of 127 networks. Use a default subnet mask of 255.0.0.0 
Class B 	128.1.0.1 to 191.255.255.254 	Supports 65,000 hosts on each of 16,000 networks. Use a default subnet mask of 255.255.0.0 
Class C 	192.0.1.1 to 223.255.254.254 	Supports 254 hosts on each of 2 million networks. Use a default subnet mask of 255.255.255.0 
Class D 	224.0.0.0 to 239.255.255.255 	Reserved for multicast groups. 
Class E 	240.0.0.0 to 254.255.255.254 	Reserved for future use, or research and development purposes. 

