The NS IP Address for Facebook, Google and Tesla
        
        FACEBOOK; 102.132.101.35
        
        GOOGLE; 216.58.223.238
        
        TESLA; 23.9.66.10

Breakdown the following RFC 1918 ipv4 address range into exactly 4 subnetwork with no address left over;
        
        
        i. 10.10.10.0
            submask = 255.0.0.0 (class A)
            binary: 11111111.00000000.00000000.00000000
            formular for number of subnet = 2^n
                where n = number of bits
                for 4 subnet
                    4 = 2^n
                    hence n = 2
            binary: 11111111.11000000.00000000.00000000
            CIDR: 10.10.10.0/10
            new submask = 255.192.0.0
             AND operation of binary on initial ip address and binary of new submask
                00001010.00001010.00001010.00000000
                11111111.11000000.00000000.00000000
                =00001010.00000000.00000000.00000000
                therefore new ntwork id = 10.0.0.0
                host range: 10.0.0.1 - 10.0.0.254
                broadcast id = 10.0.0.255

        ii. 192.168.0.0
                submask = 255.255.255.0 (class C)
                binary: 11111111.11111111.11111111.00000000
                no of subnet: 4=2^n
                    hence n = 2
                    therefore: 11111111.11111111.11111111.11000000
                    CIDR = 192.168.0.0/26
                    new submask = 192.168.192.0
                    AND operation of binary of initial ip address and new submask
                        11000000.10101000.11000000.00000000
                    AND
                        11000000.10101000.00000000.00000000
                    new network id = 198.168.0.0
                    number of host= 2^n-2
                        2^6(-2)=62
                    host range 192.168.0.1 - 192.168.0.62
                    broadcast id = 192.168.0.63
            
        iii. 172.168.1.0
                submask = 255.255.0.0 (class C)
                            11111111.11111111.00000000.00000000
                            no of subnet: 2^n = 4
                                hence n = 2
                            therefore:
                                11111111.11111111.11000000.00000000
                                CIDR 172.168.1.0/18
                                new submask: 255.255.192.0
                                AND operation
                                    therefore network id = 172.168.0.0
                                    host range = 172.168.0.1 - 172.168.0.254
                                    broadcast id = 172.168.0.255    

