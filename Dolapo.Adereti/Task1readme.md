<h1> TCP/IP Model </h1>
<br>
The Transmission Control Protocol/Internet Protocol [TCP/IP] is a suite communication protocol used to interconnect network devices on the internet. It specifies how data is exchanged over the internet by providing end-to-end communications that identify how it should be broken into packets, addressed, transmitted, routed, and received at the destination. TCP/IP requires little central management and is designed to make networks reliable with the ability to recover automatically from the failure of any device on the network. <br>
The two main protocols in the IP suite serve specific functions. TCP defines how applications can create channels of communication across a network. It also manages how a message is assembled into smaller packets before they are then transmitted over the internet and reassembled in the right order at the destination address. IP defines how to address and route each packet to make sure it reaches the right destination. Each gateway computer on the network checks this IP address to determine where to forward the message. <br>
<br>
<h2> The 4 layers of the TCP/IP model </h2>

TCP/IP functionality is divided into four layers, each of which includes specific protocols:

<p>
<b> 1. Network Access/Physical Layer – </b>
This layer corresponds to the OSI model's combination of the Data Link Layer and Physical Layer. It looks out for hardware addressing and the protocols present in this layer allow for the physical transmission of data.  It is the topmost layer in the TCP/IP model and is responsible for handling high-level protocols, and issues of representation. This layer allows the user to interact with the application. When one application layer protocol wants to communicate with another application layer, it forwards its data to the transport layer. Some of the main protocols used in the application include HTTP (HTTP stands for Hypertext transfer protocol), SNMP (Simple Network Management Protocol, a framework used for managing the devices on the internet by using the TCP/IP protocol suite), SMTP (Simple mail transfer protocol), DNS (Domain Name System), FTP (File Transfer Protocol). </p>
<p>

<b> 2. Internet Layer – </b>
This layer parallels the functions of OSI’s Network layer. It defines the protocols which are responsible for the logical transmission of data over the entire network. The main protocols residing at this layer are: <br>
•  <i>	IP (Internet Protocol) </i> – It is responsible for delivering packets from the source host to the destination host by looking at the IP addresses in the packet headers. IP has 2 versions, IPv4 and IPv6. IPv4 is the one that most websites currently use. But IPv6 is growing as the number of IPv4 addresses is limited in number when compared to the number of users. <br>
• <i>	ICMP </i> – stands for Internet Control Message Protocol. It is encapsulated within IP datagrams and is responsible for providing hosts with information about network problems. <br>
• <i>	ARP </i> – stands for Address Resolution Protocol. Its job is to find the hardware address of a host from a known IP address. ARP has several types: Reverse ARP, Proxy ARP, Gratuitous ARP, and Inverse ARP.
</p>

<p>
<b> 3. Host-to-Host/Transport Layer – </b>
This layer is analogous to the transport layer of the OSI model. It is responsible for end-to-end communication and error-free delivery of data. It shields the upper-layer applications from the complexities of data. The two main protocols present in this layer are: <br>
 	 • <i>Transmission Control Protocol (TCP) – </i> It is known to provide reliable and error-free communication between end systems. It performs sequencing and segmentation of data. It also has an acknowledgment feature and controls the flow of the data through a flow control mechanism. It is a very effective protocol but has a lot of overhead due to such features. Increased overhead leads to increased costs.
    <br>
 	• <i> User Datagram Protocol (UDP) – </i> On the other hand does not provide any such features. It is the go-to protocol if your application does not require reliable transport as it is very cost-effective. Unlike TCP, which is a connection-oriented protocol, UDP is connectionless.
</p>

<p>
<b> 4. Application Layer – </b>
This layer performs the functions of the top three layers of the OSI model: Application, Presentation, and Session Layer. It is responsible for node-to-node communication and controls user-interface specifications. Some of the protocols present in this layer are HTTP, HTTPS, FTP, TFTP, Telnet, SSH, SMTP, SNMP, NTP, DNS, DHCP, NFS, X Window, and LPD. <br>
 • <i>	HTTP and HTTPS (Hypertext transfer protocol) – </i> It is used by the World Wide Web to manage communications between web browsers and servers. HTTPS stands for HTTP-Secure. It is a combination of HTTP with SSL(Secure Socket Layer). <br>
 • <i>	SSH ( Secure Shell) – </i> It is a terminal emulations software and is preferred because of its ability to maintain an encrypted connection. It sets up a secure session over a TCP/IP connection. <br>
 • <i>	NTP (Network Time Protocol) – </i> It is used to synchronize the clocks on our computer to one standard time source. It is very useful in situations like bank transactions.
 </p>