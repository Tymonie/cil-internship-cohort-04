# TCP/IP model.

### What is the TCP/IP?

* TCP/IP is actually a combination of two separate protocols TCP and IP. TCP stands for **Transmission Control Protocol** a communications standard that enables application programs and computing devices to exchange messages over a network. It is designed to send packets across the internet and ensure the successful delivery of data and messages over networks.
It ensures end-to-end data delivery. TCP organizes data so that it can be transmitted between a server and a client.

* The Internet Protocol (IP) is the method for sending data from one device to another across the internet. Every device has an IP address that uniquely identifies it and enables it to communicate with and exchange data with other devices connected to the internet. IP is responsible for defining how applications and devices exchange packets of data with each other.

TCP/IP (Transmission Control Protocol/Internet Protocol) is a set of standard rules or protocols which allows computing devices to communicate with one another over a network. It specifies how information is shared between devices on a network, how they should be packaged, sent and received.

TCP and IP are separate protocols that work together to ensure data is delivered to its destination within a network. IP obtains and defines the address—the IP address—of the application or device the data must be sent to. TCP is then responsible for transporting and routing data through the network architecture and ensuring it gets delivered to the destination application or device that IP has defined. 

In other words, the IP address is akin to a phone number assigned to a smartphone. TCP is the computer networking version of the technology used to make the smartphone ring and enable its user to talk to the person who called them. The two protocols are frequently used together and rely on each other for data to have a destination and safely reach it, which is why the process is regularly referred to as TCP/IP.

### TCP/IP Model

the TCP/IP model is based on the OSI model although it is considered less rigid than the OSI model, the TCP/IP model consist of 4 layers which are:
* **application -  layer 4**
* **transport - layer 3**
* **internet - layer 2**
* **datalink - layer 1**

1. **application layer:** The application layer refers to programs that need TCP/IP to help them communicate with each other. This is the level that users typically interact with, such as email systems and messaging platforms. It combines the session, presentation, and application layers of the OSI model.

2. **transport layer:** The transport layer is responsible for providing a solid and reliable data connection between the original application or device and its intended destination. This is the level where data is divided into packets and numbered to create a sequence. The transport layer then determines how much data must be sent, where it should be sent to, and at what rate. It ensures that data packets are sent without errors and in sequence and obtains the acknowledgment that the destination device has received the data packets.

3. **internet layer:** The internet layer is responsible for sending packets from a network and controlling their movement across a network to ensure they reach their destination. It provides the functions and procedures for transferring data sequences between applications and devices across networks.

4. **datalink layer:** The datalink layer defines how data should be sent, handles the physical act of sending and receiving data, and is responsible for transmitting data between applications or devices on a network. This includes defining how data should be signaled by hardware and other transmission devices on a network, such as a computer’s device driver, an Ethernet cable, a network interface card (NIC), or a wireless network

### TCP/IP model vs. OSI model

TCP/IP and OSI are the most widely used communication networking protocols. The main difference is that OSI is a conceptual model that is not practically used for communication. Rather, it defines how applications can communicate over a network. TCP/IP, on the other hand, is widely used to establish links and network interaction. TCP/IP model and the OSI model share some similarities which are:

### Similarities between TCP/IP and OSI model

* They are both logical models.
* They define networking standards.
* They divide the network communication process in layers.
* They provide frameworks for creating and implementing networking standards and devices.
* They enable one manufacturer to make devices and network components that can coexist and work with the devices and components made by other manufacturers.

### differences between TCP/IP and OSI model

* TCP/IP uses just one layer (application) to define the functionalities of the upper layers, while OSI uses three layers (application, presentation and session).
* TCP/IP uses one layer (physical) to define the functionalities of the bottom layers, while OSI uses two layers (physical and data link).V
* TCP/IP is a protocol-oriented standard, whereas OSI is a generic model based on the functionalities of each layer.
* In TCP/IP, the protocols were developed first, and then the model was developed. In OSI, the model was developed first, and then the protocols in each layer were developed.
* TCP/IP helps establish a connection between different types of computers, whereas OSI helps standardize routers, switches, motherboards and other hardware.

