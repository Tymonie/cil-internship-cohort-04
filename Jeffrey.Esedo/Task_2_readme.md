
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
