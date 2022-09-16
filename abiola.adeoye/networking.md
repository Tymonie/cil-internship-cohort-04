# What are the NS IP addresses for Google, Facebook and Tesla?

* **Google:** 216.58.223.206 (google.com)

* **Facebook:** 102.132.101.35 (facebook.com)

* **Tesla:** 104.75.172.54 (tesla.com)

# Breakdown the following RFC 1918 IPv4 address range into exactly 4 subnetwork with no address left over

### **10.10.10.0**
IPV4 class A (range 0-127), it has a default subnet mask of 255.0.0.0/8.
For 4 subnetwork the subnet mask will be /10 which gives (255.192.0.0), therefore:

* Network ID: 10.0.0.0, 10.64.0.0, 10.128.0.0, 10.192.0.0

* Host ID range: (10.0.0.1 - 10.63.255.254), (10.64.0.1 - 10.127.255.254), (10.128.0.1 - 10.191.255.254), (10.192.0.1 - 10.255.255.254)

* Broadcast ID: 10.63.255.255, 10.127.255.255, 10.191.255.255, 10.255.255.255

### **192.168.0.0**
IPV4 class C (range 192-223), it has a subnet mask of 255.255.255.0/24
For 4 subnetwork the subnet mask will be /26 which gives (255.255.255.192), therefore:

* Network ID: 192.168.0.0, 192.168.0.64, 192.168.0.128, 192.168.0.192

* Host ID range: (192.168.0.1 - 192.168.0.62), (192.168.0.56 - 192.168.0.126), (192.168.0.129 - 192.168.0.190), (192.168.0.193 - 192.168.0.254)

* Broadcast ID: 192.168.0.63, 192.168.0.127, 192.168.0.191, 192.168.0.255


### **172.168.1.0**
IPV4 class B (range 128-191), it has a default subnet mask of 255.255.0.0/16.
For 4 subnetwork the subnet mask will be /18 which gives (255.255.192.0), therefore:


* Network ID: 172.168.0.0, 172.168.64.0, 172.168.128.0, 172.168.192.0

* Host ID range: (172.168.0.1 - 172.168.63.254), (172.168.64.1 - 172.168.127.254), (172.168.128.1 - 172.168.191.254), (172.168.192.1 - 172.168.255.254)

* Broadcast ID: 172.168.63.255, 172.168.127.255, 172.168.191.255, 172.168.255.255

