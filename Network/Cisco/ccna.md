# CCNA

<https://www.youtube.com/watch?v=l2pr-GAxxW4>

## Module 2

### General Concepts

- Layer 1: NIC card or Hub
- Layer 2: MAC Address
  - Burned-in Addresses (BIA)
  - 48 bit address
  - Hex (16 bit)
  - First 24 bits are the Organization Unique ID (OUI)
  - Second 24 bits are unique value (MAC)
- Layer 2 Switches
  - Sends FRAMES
  - Each port is a collition domain
  - Builds a map of MAC address to port
  - Switches increase the number of collition domains
- Layer 3 Addressing
  - Logical IP address (SW)
  - Assigned manually or via DHCP
  - Routers look at the network portion of the address
  - If the address is not in the routing table, the packet is discarted
- IPv4 addressing
  - 32 binary bits / 4 octets (8bits)
  - Each octect separated by a dot
- IPv6 
  - 128 bits long
  - Written in hex
  - 16 bits separated by colons
- Routing
  - Choosing best path for traffic = routing
  - Sending traffic = switching 
  - Router connected with layer 2 and 3 only
  Router encapsulated packet with the correct header for media type
- Domain: specific part of the network
- Bandwidth: Amount of data a link can carry in X msec
- Unicast: Data sent to one device
- Multicast: Data sent to a group of devices
- Broadcast: Data sent to all devices
- Collision domain: Devices sharing the same bandwidth
- Broadcast domain: Devices receiving the same broadcast message.

### OSI Modle

### TCP Model

- TCP Layers
  - Application
    - Maps to Applications, Session, and Presentation
    - SMTP (TCP:25), POP3 (TCP:110), HTTP (TCP:80), FTP (TCP:20data 21control), SNMP, DHCP, TFTP (UDP:69), DNS (TCP/UDP:53), Telnet (TCP:23)
  - Transport
    - TCP connection oriented, reliable data transfer
    - UDP unreliable, connectionless data transfer. Less overhead then TCP
    - Port numbers Identifies traffic type. 65532 in total, but 0 - 1023 well known
    - TCP Three-Way Handshake: SYN, SYN-ACK, ACK
  - Internet
    - Maps to L3
    - Includes IP the connectionless protocol (IPv4 and IPv6)
    - Includes ICMP (ping)
  - Network Access Layer
    - Comprises Data Link and Physical Layer
    - ARP: Requests MAC address of host with known IP address
    - Data link
    - Physical

### TCP/IP Protocols and Services

- RDP
- SNMP UDP:161/162
- ICMP
- IGMP
- TCP
- UDP
- ARP
  - Address Resolution Protocol
  - Allows hosts to learn the layer 2 address based on layer 3 address
  - Host broadcasts ARP request onto the cable
  - Switch forwards out of all ports
  - Destination host sends ARP reply with its layer 2 address
  - PC can now encapsulate frames with correct address

### LAN Technology

- 10BaseT: Cat3 cable and distance of 100m
- 100BaseT: FastEthernet, Cat5 cable and distance of 100
- 100BaseFX: Two strands of fiber cables
- 1000BaseT: Cat5, 5e or 6. Uses all 4 pairs of UTP cable
- 1000BaseX: Fiber for 1Gbps speeds
- 10GBaseT: Cat6 up to 55m and Cat6a up to 100m

- 10GBaseSR: Sort range 80-300m
- 10GBaseLR: Long range, single mode fiber, up to 25Km 
- 10GBaseER: Extended range, up to 40km

- 10GBaseSW
- 10GBaseLW
- 10GBaseEW 

- CSMA/CA
  - Used on wireless networks where end device cannot detect signal
  - Carrier Sense
  - Multiple Access
  - Collision Avoidance - clear signal send from Access Point
  - RTS: Ready ro Send signal sent from node
  - CTS: Clear to Send signal from the AP