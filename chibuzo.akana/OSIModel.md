## Describe any layered process you are familiar with similar to the OSI model

 The Open System Interconnection (OSI) model is a framework that is used to describe how computer network functions. 
It has 7 layers that functions using a top-down construction and vice versa. 

**•	At layer 1 - Physical Layer** 
From the name, it's the layer that deals with the Physical requirements of the network that facilitates data transfer such as radio links, routers, switches installed in the network.

**•	Layer 2 - Data Link Layer**
This layer is responsible for transferring information between two physically connected devices. It has two sublayers: 
*i. Media Acces Control(MAC)* - which determines how devices in a network gain access to a medium and permission to transmit data. 
*ii. Logical Link Control (LLC)* - identifies network layer protocols and controls error checking to ensure successful transmission. 

**•	Layer 3 - Network Layer** 
This layer is responsible for arranging the data on the sender's device and reassemble it on the recipient's device when the transmission is across two different networks. This layer is basically for 
*a. Logical Addressing* - which involves IP addressing.
*b. Routing* - the moving of packets from source to destination.
*c. Path determination* - choosing the best path for data delivery.

**•	Layer 4 - Transport Layer**
Transport layer takes and breaks data into segments known  as segmentation. It controls the reliability of communication through flow control by managing the size of data being transmitted. 

**•	Layer 5 - Session Layer**
This layer helps in managing sessions such as ensuring a file is completely transferred and retransmitted should the file be incomplete. This transfer makes communication over a network more efficient and reduce wasting resources or transferring the entire file again. 


**•	Layer 6 - Presentation Layer**
The presentation layer prepares data to be displayed to the user. This layer is responsible for compressing and decompressing data as it moves from one device to another.

**•	Layer 7 - Application Layer**
This is the layer that provides for network applications with the help of protocol to provide user activities. 

From the sender data flows from layer 7 to layer 1 and from the layer 1 to layer 7 on the recipient's device. 

Using an email application - a sender sends an email, the presentation layer compresses the message and sends the message to the session layer, which opens a session for communication between the sender and the outgoing server.

The transport layer receives the message and segments it. The network layer breaks the segments into packets. The data link layer receives the packets further breaks them down into frames. The frames are sent to the physical layer where data is converted into ones and zeros and transferred across medium as such as cables.

When the message reaches the recipient. The process is reversed and data is sent from the physical layer to the application layer where data is converted form ones and zeros to message available in the recipient's email.

The top-down and down-top movement describes the flow of data in the OSI model.

