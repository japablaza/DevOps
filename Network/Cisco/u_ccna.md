# CCNA

## The Transport Layer

- TCP
  - Transport Control Protocol
  - TCP is connection oriented
  - TCP carries out sequencing to ensure segments areprocessed in the correct order
  - TCP is reliable - the receicing host sends acks back to the sender. Lost segments are resent
  - TCP performs flow control
  - TCP uses the Three-Way Handshake
    - SYN, ACK/SYN, ACK
- TCP Header
  - Source Port (16 bits)
  - Destination Port (16 bits)
  - Sequence Number (32 bits)
  - Ack Number (32 bits)
  - Header Length (4 bits)
  - Reserved (6 bits)
  - Code Bits (6 bits)
  - Windows (16 bits)
  - Checksum (16 bits)
  - Urgent (16 bits)
  - Options (0 to 32 bits)
  - Data (Varies)

- UDP
  - User Datagram Protocol sends traffic best effort
  - UDP is not connection oriented. There is no handshake
  - UDP does not carry out sequencing
  - UDP is not reliable. The receiving host does not send acks back to the sender
  - UDP does not perform flow control
  - If error detection and recovery is required, it is up to the upper layers to provide it. 
- UDP Header
  - Source Port
  - Destination Port
  - Length
  - UDP checksum
  - Data

## The Network Layer (L3)

- Routing packets to destination and QoS
- IP is layer 3 protocol
- IP is connectionless protocol with no ACK at L3
- IP Addressing
- IP header
  - 32 bit
    - Version 4 bits
    - hdr 4 bit
    - Type of service
    - ID 16 bit
    - flags 3 bit
    - Fragment offset 13 bit
    - TTL 8 bit
    - Protocol 8 bit
    - Checksum 16 bit
    - Source 32 bit
    - Destination 32 bit
    - Header options ( 0-40 bytes )
    - Data ( variable length )

- Unicast traffic goes to a single destination host
- Broadcast traffic goes to all host on the subnet
- Multicast traffic goes to multiple interested hosts

## IP Address Class

- Class A
  - Default mask is /8
  - Valid network address range from 1.0.0.0 to 126.0.0.0/8
  - `0`xxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
  - 0.0.0.0/8 reserved and signifies `this network`
  - 0.0.0.1 to 0.255.255.255 are not valid host addresses
  - 127.0.0.0/8 reserved as the loopback address
- Class B
  - Default mask is /16
  - Valid network address range from 128.0.0.0 to 191.255.0.0/16
  - `1``0`xxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
- Class C
  - Default mask is /24
  - Valid network address range from 192.0.0.0 to 223.255.255.0/24
  - `1``1``0`xxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
- Private Addresses
  - Class A: 10.0.0.0 to 10.255.255.255
  - Class B: 172.16.0.0. to 172.31.255.255
  - Class C: 192.168.0.0 to 192.168.255.255
- Class D
  - Multicast address
  - Valid network address range from 224.0.0.0 to 239.255.255.255
  - These addresses are not allocated to hosts and there is no default subnet mask
  - `1``1``1``0`xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx
- Class E
  - Experimental and reserved for future use
  - Valid network address range from 240.0.0.0 to 255.255.255.255
  - 255.255.255.255 is the broadcast address for this network
  - `1``1``1``1`xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx

## CIDR

- Classless Inter-Domain Routing
- Subnetting
  - 

## Varialble Length Subnet Masks VLSM

- 