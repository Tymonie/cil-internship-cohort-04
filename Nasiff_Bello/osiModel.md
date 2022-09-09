## TCP/IP Model

TCP/IP model is practical model and is used in the Internet. TCP/IP is acronym of Transmission Control Protocol and Internet Protocol.
The TCP/IP model combines the first three layer of the OSI (Application, Presentation and Session layer) into one layer i.e. Application Layer and also combines the last two layers of the OSI model (Physical and Data link layer) into one layer i.e. Network Access /Host-to-Network layer. The following diagram shows the various layers of TCP/IP model:

- APLLICATION LAYER
- TRANSPORT LAYER
- INTERNET LAYER
- NETWORK ACCESS LAYER 

### Application Layer
This layer is same as that of the OSI model and performs the following functions:
* It provides different services such as manipulation of information in several ways, retransferring the files of information, distributing the results etc.
* The functions such as LOGIN or password checking are also performed by the application layer.
### Transport Layer
It does the same functions as that of transport layer in OSI model. Here are the key points regarding transport layer:
* It uses TCP and UDP protocol for end to end transmission.
* TCP is reliable and connection oriented protocol.
* TCP also handles flow control.
* The UDP is not reliable and a connection less protocol also does not perform flow control.
### Internet Layer
The internet layer has the task of exchanging datagrams across network boundaries. It is therefore also referred to as the layer that establishes internetworking, indeed, it defines and establishes the Internet. This layer defines the addressing and routing structures used for the TCP/IP protocol suite. The primary protocol in this scope is the Internet Protocol, which defines IP addresses. Its function in routing is to transport datagrams to the next IP router that has the connectivity to a network closer to the final data destination 
The function of this layer is to allow the host to insert packets into network and then make them travel independently to the destination. However, the order of receiving the packet can be different from the sequence they were sent.
### The Network Access Layer / Host-to-Network Layer 
The Network Access layer of the TCP/IP model corresponds with the Data Link and Physical layers of the OSI reference model. It defines the protocols and hardware required to connect a host to a physical network and to deliver data across it. This protocol varies from host to host and network to network. Packets from the Internet layer are sent down the Network Access layer for delivery within the physical network. The destination can be another host in the network, itself, or a router for further forwarding. So the Internet layer has a view of the entire Internetwork whereas the Network Access layer is limited to the physical layer boundary that is often defined by a layer 3 device such as a router.

### Similarities between OSI and TCP / IP Reference Models
*  Both the reference models are based upon layered architecture.
*  The layers in the models are compared with each other. The physical layer and the data link layer of the OSI model correspond to the link layer of the TCP/IP model. The network layers and the transport layers are the same in both the models. The session layer, the presentation layer and the application layer of the OSI model together form the application layer of the TCP/IP model.
* In both the models, protocols are defined in a layer-wise manner.
* In both models, data is divided into packets and each packet may take the individual route from the source to the destination.

### Differences between OSI and TCP / IP Reference Models
* OSI model is a generic model that is based upon functionalities of each layer. TCP/IP model is a protocol-oriented standard.
* OSI model distinguishes the three concepts, namely, services, interfaces, and protocols. TCP/IP does not have a clear distinction between these three.
* OSI model gives guidelines on how communication needs to be done, while TCP/IP protocols layout standards on which the Internet was developed. So, TCP/IP is a more practical model.
* In OSI, the model was developed first and then the protocols in each layer were developed. In the TCP/IP suite, the protocols were developed first and then the model was developed.
* The OSI has seven layers while the TCP/IP has four layers.

The following diagram shows the corresponding layers of OSI and TCP/IP models 
|  OSI MODLE               |         TCP/IP
---------------------------|--------------------------------
| APPLICATION LAYER        |        APPLICATION LAYER
| PRESENTATION LAYER       |      
| SESSION LAYER            |
| TRANSPORT LAYER          |         TRANSPOERT LAYER
| NETWORK LAYER            |         INTERNET LAYER
| DATA LINK LAYER          |         NETWORK ACCESS LAYER
| PHYSICAL LAYER           |    

 
