# TCP/IP Model

The TCP/IP model is a concise version of the OSI model. It contains four layers, unlike seven layers in the OSI model. The layers are:
* Process/Application Layer
* Host-to-Host/Transport Layer
* Internet Layer
* Network Access/Link Layer

## Network Access Layer –
This layer corresponds to the combination of Data Link Layer and Physical Layer of the OSI model and it looks out for hardware addressing and the protocols present in this layer allows for the physical transmission of data.

##  Internet Layer –
This layer parallels the functions of OSI’s Network layer. It defines the protocols which are responsible for logical transmission of data over the entire network. The main protocols residing at this layer are :
* IP (Internet Protocol)
* ICMP (Internet Control Message Protocol)
* ARP (Address Resolution Protocol)

## Host-to-Host Layer –
This layer is analogous to the transport layer of the OSI model. It is responsible for end-to-end communication and error-free delivery of data. It shields the upper-layer applications from the complexities of data. The two main protocols present in this layer are :
* Transmission Control Protocol (TCP)
* User Datagram Protocol (UDP)

## Application Layer –
This layer performs the functions of the Application, Presentation, and Session layer of the OSI model. It is responsible for node-to-node communication and controls user-interface specifications. Some of the protocols present in this layer are: HTTP, HTTPS, FTP, TFTP, Telnet, SSH, SMTP, SNMP, NTP, DNS, DHCP, NFS, X Window, LPD. 