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







