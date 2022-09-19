# THE OSI MODEL

The OSI model stands for **open system interconnection model** and it's a system that helps us to understand how computers interact with each other in a network. 

There are a lot of high-level functionalities at play when computers interact with each other but the OSI model helps us narrow down those functionalities into seven layers and this helps with problem-solving for IT engineers as they can just identify which layer a particular problem belongs to and work on it. 

These layers are: 

 - Application Layer  
 - Presentation Layer  
 - Session Layer 
 - Transfer Layer  
 - Network Layer 
 - Data link 
 - Physical layer

 

My focus will be on the Presentation layer. 

The Presentation layer is also known as the **"translation layer"**, because data going to and fro the application layer is not often in the format required to be transported, this layer sees to it that data is transported properly through: 

- **Data Translation:** Translates the data received from the application layer (stored in letters and numbers)  into machine readable language.

- **Data Compression:** This breaks down the data being sent out into smaller bits before it's sent out. In summary, it reduces data size. 

- **Data Encryption/Decryption:** Before the data is finally sent out it is encrypted in a way that only the computer/person authorized to access the data can decrypt it upon arrival, this ensures data is transported without a security breach.

  