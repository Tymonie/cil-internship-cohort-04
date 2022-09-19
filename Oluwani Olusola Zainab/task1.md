# PRESENTATION LAYER

Presentation layer receives data from application layer, this data is in form of numbers and characters. Presentation layer translates this data to machine understandable binary format e. g. Conversion of ASCII => EBCDIC. 
This process is called TRANSLATION. Before data is transmitted, presentation layer reduces the number of bit that are used to represent original data, this process is called DATA COMPRESSION. It can be loose or loseless. 
Data compression reduces the amount of space used to store the original file, as the size of file is reduced, it can be received at the destination in a very less time. To maintain the integrity of data, before transmission data is ENCRYPTION. Encryption enhances the security of sensitive data. At sender side data is encrypted, at receiver side data is decrypted. Secure Sockets Layer (SSL) is used in presentation layer for encryption and decryption. 
So presentation layer performs three basic functions:
1. Translation
2. Data Compression 
3. Encryption / Decryption
