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

## The Network Layer