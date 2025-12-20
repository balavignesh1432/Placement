# Computer Networks

## Introduction

- **Network**: A group of connected computers and devices that can communicate and share data.
- **Node**: Any device that can send, receive, or forward data in a network. Ex: Computer, Router
- **Wired media**: Ethernet cables, optical fibre.
- **Wireless media**: Wi-Fi, Bluetooth

---

## Network Architectures

### Peer-to-Peer Architecture (P2P)

In P2P (Peer-to-Peer) Architecture, there is not any concept of a Central Server. Each device is free for working as either client or server.

- Each computer in the network has the same set of responsibilities and capabilities.
- Each computer in the network has the ability to share data with other computers in the network.
- **Not Reliable**: Because of no central server, data is always vulnerable to getting lost because of no backup.

### Client-Server Model

The Client-Server Model is a distributed architecture where clients request services and servers provide them.

- **Scalability**: Servers and clients can scale independently.
- **Security**: Centralized security policies and authentication.

---

## Network Types

- **Personal Area Network (PAN)**: 1 to 10 metres. Ex: Bluetooth
- **Local Area Network (LAN)**: Building, Campus. Ex: University Network
- **Metropolitan Area Network (MAN)**: City. Ex: Cable Network
- **Wide Area Network (WAN)**: Country, Continent. Ex: Internet

---

## Network Topologies

Network Topologies: Layout of the network

- **Bus** – All devices share a single backbone cable. Backbone fails the topology crashes.
- **Star** – All devices connect to a central hub/switch. Hub fails the whole topology fails.
- **Ring** – Devices form a closed loop, data flows in one direction. Single Node fails the whole topology fails.
- **Mesh** – Devices are interconnected with multiple paths. Robust but high efforts.
- **Tree** – Hierarchical combination of star and bus. Data flow from Top to Bottom. Backbone fails the topology crashes.
- **Hybrid** – Combination of two or more topologies.

---

## Internetworking & Network Types

**Internetworking**: Connecting multiple networks.

### Intranet

- Private network used within an organization.
- Ex: Company HR portal.

### Extranet

- Provides limited access to external partners. (Inter-organization collaboration)
- Requires Authentication/VPN.
- Ex: Customer order-tracking portals

---

## Data Transmission Modes

- **Unicast**: One sender → one specific receiver
- **Broadcast**: One sender → all devices in the network
- **Multicast**: One sender → a selected group of receivers
- **Anycast**: One sender → the nearest (best) receiver from a group

---

## Network Devices

### Layer 1 Devices: Physical Layer

Work with raw electrical (bits) or optical signals. They are "dumb" devices that do not understand IP addresses or MAC addresses.

- **Hub**: It takes an incoming signal on one port and blindly broadcasts it to all other ports. It does not know who the recipient is.
- **Repeater**: It receives a weak signal (due to attenuation over long cables), amplifies it, and retransmits it.
- **Modem** (Modulator-Demodulator): Connects your home network to the ISP (Internet Service Provider). Converts digital signals from your computer into analog signals for telephone/cable lines (Modulation) and vice-versa (Demodulation).

### Layer 2 Devices: Data Link Layer

Work with MAC Addresses.

- **Switch**: Connects devices within a LAN. Learns the MAC address of every connected device. It sends data only to the specific port where the destination device is connected. Maintains a MAC address table.
- **Bridge**: Connects two separate LAN segments to make them appear as one. Learns MAC addresses and builds a bridge table. (Obsolete)

### Layer 3 Devices: Network Layer

Work with IP Addresses.

- **Router**: Connects different (Similar IP - IP) networks and forwards packets based on IP addresses. (LAN-WAN Communication). Chooses the best path using routing tables.

### Layer 4-7 Devices

- **Gateway**: Connects dissimilar networks using different protocols (Protocol Converter). An Internet Gateway connects a private network to the public Internet and allows traffic to flow in and out.

- **Firewall**: Security Hardware/Software. Controls incoming and outgoing traffic based on security rules. (Packet Filtering)

---

## OSI (Open Systems Interconnection) Model

Set of rules that explains how different computer systems communicate over a network. Consists of 7 layers and each layer has specific functions and responsibilities.

---

### Layer 1: Physical Layer (PL)

Responsible for transmitting individual bits from one node to the next (Inside Network).

- Modulation to prepare the data for transmission and demodulation to retrieve it at the other end.
- **Protocols** (IEEE 802): Ethernet, Wi-Fi, Bluetooth

#### Transmission Modes

- **Simplex (Uni Directional)**: Only one of the two devices on a link can transmit, the other can only receive.
- **Half Duplex**: Each node can transmit and receive, but not at the same time. The entire capacity of the channel can be utilized for each direction.
- **Full Duplex**: Both stations can transmit and receive simultaneously. Capacity of the channel must be divided.

---

### Layer 2: Data Link Layer (DLL)

Makes sure data transfer is error-free from one node to another, over the physical layer.

- Ensure error-free transmission of information.
- **LLC (Logical Link Control)**: Flow Control and Error Control.
- **MAC (Media Access Control)**: Framing and MAC Addressing. Prevents collisions using access methods.

#### Frame Structure

- Packet in the Data Link layer is referred to as **Frame**.
- Adds MAC addresses of the sender and receiver in the header of each frame.
- The Receiver's MAC address is obtained by placing an **ARP (Address Resolution Protocol)** request.
- Adds Error Detection Codes to each Frame.

#### Error Detection

Ensure data frames are delivered accurately from sender to receiver.

##### Parity Bit

- No. of ones odd = 1, even = 0.

##### Checksum

- **On Sender**: Add segments, calculate sum, complement to get checksum. Send Checksum with data.
- **On Receiver**: Add segments, calculate sum, add with checksum, and complement to get all 0s.

##### Cyclic Redundancy Check (CRC)

Based on Binary Division.

- **Sender**: Data becomes divisible by check bits. CRC added to data.
- **At the destination**: The incoming data is divided by CRC. Remainder 0 check.

#### Error Correction

##### Hamming Code

- Receiver uses hamming code parity bits to correct the message.
- Redundant bits are placed on powers of 2 positions.

#### Flow Control

Fast sender might overwhelm a slow receiver, causing data loss or inefficient communication.

##### Stop-and-Wait

- Sender transmits one frame and waits for an acknowledgment before sending the next.

**With Automatic Repeat Request (ARQ)**:

- If the sender does not receive an ACK within timeout, it assumes that the frame was lost and retransmits the frame.
- Sequence number is also added to prevent confusion when delayed acknowledgements.

##### Sliding Window

Sends window of frames. The sender keeps track of a "window" of unacknowledged frames, sliding it forward as acknowledgments arrive to send new frames continuously.

**With Go Back N** (Achieved through Sequence Numbers):

- **Sender**: If a packet is lost, the sender retransmits that packet and all subsequent packets in the window.
- **Receiver**: If an out-of-order packet arrives: discards it and resends ACK for the last correctly received packet.

**With Selective Repeat**: Only retransmitting packets that are lost or corrupted. (Achieved via equal window on both sides)

- Requires a full-duplex link, allowing data to be sent in both directions simultaneously.
- **Sender**: Retransmits specific packets that were not acknowledged after a timeout.
- **Receiver**: Accepts and buffer packets that arrive out of order.

##### Piggybacking (In Full Duplex)

When a data frame arrives, the receiver can delay sending an ACK and attach it to its next outgoing data frame, reducing the number of separate messages and improving network efficiency.

#### Media Access Control Protocols

**CSMA (Carrier Sense Multiple Access)** protocol controls access to a shared medium.

##### CSMA/CD (Collision Detection)

Used in Wired.

1. Station checks if the channel is idle, then transmits
2. If collision occurs, transmission stops
3. Then Jam Signal sent
4. Exponential Backoff, then retransmit
5. Collisions are detected after they occur

##### CSMA/CA (Collision Avoidance)

Used in Wireless.

1. Station listens to the channel. If busy → wait
2. If idle then waits for a small fixed time called **IFS (Inter Frame Space)**
3. This ensures priority for important frames (ACK, CTS)
4. Then Backoff timer (Random) decreases only when channel is idle
5. If channel becomes busy, Timer pauses and Resumes when channel is idle again
6. When backoff timer reaches zero, Device transmits the frame

---

### Layer 3: Network Layer

Ensures data travels from the source to the destination even if they are on different networks.

- Encapsulates transport layer segments into packets with source and Destination IP.
- Routers analyze the destination address and determine the best available path. (Hops)

#### Internet Protocol (IP)

Set of rules that allows devices to communicate over the Internet. It ensures that information sent from one device reaches the correct destination by using a unique set of numbers known as IP addresses.

##### IP Packet Structure

- **Header**: The header contains source and destination IP addresses, that helps routers determine where to send the packet.
- **Payload**: The payload contains the actual data being transmitted.

##### Subnetting

Subnetting is the process of dividing one large network into smaller sub-networks (subnets). Network traffic can travel a shorter distance without passing through unnecessary routers to reach its destination.

#### IP Addressing

##### Classful IP Addressing (IPv4)

32 Bits (4 Bytes). IP addresses were divided into five classes (A, B, C, D, E).

| Class | Range | Network ID | Networks | Host ID | Hosts | Subnet Mask |
|-------|-------|------------|----------|---------|-------|-------------|
| A (Large Networks) | 0.0.0.0 | 8 Bits | 2^8 Networks | 24 bits | 2^24 hosts | 255.x.x.x |
| B (Medium Networks) | 128.0.0.0 | 16 Bits | 2^16 Networks | 16 bits | 2^16 hosts | 255.255.x.x |
| C (Small Networks) | 192.0.0.0 | 24 Bits | 2^24 Networks | 8 bits | 2^8 hosts | 255.255.255.x |
| D (Multicasting) | 224.0.0.0 | - | - | - | - | - |
| E (R&D Use) | 240.0.0.0 | - | - | - | - | - |

**Important Notes**:

- Total Host in Class is Reduced by 2.
- 1st IP address of any network is the network number. (All 0s after Subnet Mask)
- Last IP address is reserved for broadcast IP. (All 1s after Subnet Mask)

##### Classless IP

- IP address with number of bits for mask after '/' symbol, like `192.168.1.1/28`.
- Variable length mask. Minimum wastage of IP addresses.

##### IPv6

- 16 Byte (128-bit) address (virtually unlimited addresses).
- It was created to overcome the shortage and support the future growth of the internet. Improved Security.

##### Tunneling

- Allows IPv6 users to send data through an IPv4 network to reach other IPv6 users.
- Achieved by encapsulating packets.

##### IP Address Types

**Private IP Address**:
- Used for communication within a local network (LAN). Not visible on the internet.
- Assigned by a router, ensuring unique addresses for each device on the network.

**Public IP**:
- Used to communicate outside the network. Visible on the internet.
- Assigned by the ISP (Internet Service Provider).

**Dynamic IP Address**:
- Changes over time. Assigned by the ISP each time a device connects to the internet.

**Static IP Address**:
- Permanent. Often used by servers, such as DNS servers.

#### Routing

Routing refers to the process of directing a data packet from one node to another. Done by analyzing the destination IP Address of the packet.

##### Routing Types

- **Default Routing**: Transmit packets to a default route that is, a gateway, if no specific path is defined or found. Default route - `0.0.0.0/0`.
- **Static Routing**: Routers will route packets to the destination configured manually by the network administrator.
- **Dynamic Routing**: Packets are transmitted over a network using various shortest-path algorithms and pre-determined metrics. Router adds new routes to the routing table based on any changes made in the topology of the network. Consumes more bandwidth for communicating with other neighbors.

##### Routing Table

- Stores the IP addresses and relevant information regarding the nearest routers.
- The Routing Table is stored in a router that determines the shortest path and routes the data packet.
- Looks up the IP addresses of all the nodes that can transmit the packet to its destination selects the shortest path using the shortest path algorithm.

##### Routing Algorithms

**Distance-Vector Routing**:
- Nodes advertise their routing table to their adjacent nodes at regular intervals, uses Bellman Ford for shortest Path.
- Ex: **RIP (Routing Information Protocol)**

**Link-State Routing**:
- Nodes advertise their updated routing tables only when some new updates are added.
- Every router eventually learns the complete network graph.
- Uses Dijkstra algorithm for Shortest Path.
- Ex: **OSPF (Open Shortest Path First)**: OSPF is a link-state protocol that finds the shortest path using the Dijkstra algorithm.

#### Network Address Translation (NAT)

- Allows multiple devices in a private network to access the internet using a single public IP address.
- Used by routers/firewalls to translate private IP addresses into public IP addresses (and vice versa).

**Process**:

1. A device sends a request that reaches the NAT-enabled router.
2. Router replaces the private IP with its public IP and assigns a unique port.
3. NAT stores this mapping in the NAT table.
4. When the server responds, NAT uses the stored entry to send the packet to the correct internal device.

#### Supernetting

- Combining multiple smaller networks into one larger network by reducing the number of network bits.
- Reduces routing table size. Router no longer needs to store each subnet separately.
- Reduces the number of routing updates.

#### ARP (Address Resolution Protocol)

Determine the MAC address (hardware address) corresponding to an IP address. When one device in a LAN wants to communicate with another, it must know the destination's MAC address.

**Process**:

1. Sender checks ARP Cache, if the MAC address for the destination IP is already cached, communication starts immediately.
2. If not cached, the sender broadcasts an ARP request on the LAN.
3. Each device checks whether the requested IP matches its own.
4. The device with the matching IP sends an ARP reply (unicast) containing its MAC address.
5. The sender updates its ARP cache with the new MAC address for future use.

#### Reverse Address Resolution Protocol (RARP)

- Allows a device to discover its IP address when only its MAC address is known.
- Used by devices with no permanent storage to save their IP addresses.

**Process**:

1. A client broadcasts a RARP request in LAN, containing its MAC address.
2. A RARP server (or gateway router with ARP table) checks its mapping of MAC -> IP.
3. If a match is found, the server responds with the client's IP address.
4. The client configures itself with the provided IP and can now communicate on the network.

#### Dynamic Host Configuration Protocol (DHCP)

- Automates the process of assigning IP addresses and other network configuration parameters to devices joining the network.
- DHCP enables devices to join a network and automatically receive IP Address, Subnet Mask, Default Gateway, DNS Server.

**DHCP Process**:

1. Client broadcasts DHCP Discover: Who is my DHCP server?
2. DHCP server replies with: Here is an IP address I can give you, from pool of IP addresses.
3. Client requests: I want to use this IP. If multiple DHCP servers, then first offer is accepted.
4. Server confirms: IP assigned successfully with lease time. Makes an entry.

**Lease Management**:

- IP address is given for a lease time.
- Before expiry, client renews the lease. If not renewed, then IP returns to pool.

#### Internet Control Message Protocol (ICMP)

Used by network devices such as routers, gateways to send error messages and operational information.

**Error Reporting**:

- If a message cannot be delivered, ICMP informs the source about the failure.
- If a packet is too large and cannot be forwarded, the receiver drops the packet and sends an ICMP error message to the sender.

**Network Diagnostics**:

- **Traceroute**: Used to determine the path packets take across routers to reach the destination.
- **Ping**: Sends echo-request and echo-reply messages to measure round-trip time and test connectivity.

---

### Layer 4: Transport Layer

Enables end-to-end communication between applications (Processes) on different hosts.

- Implemented only in end systems, not in intermediate routers.
- Uses port numbers to identify sending and receiving applications.
- Divides data from upper layers into segments (TCP) or datagrams (UDP) and adds necessary headers.

#### Transmission Control Protocol (TCP)

Connection-oriented protocol.

- Sender and receiver remain connected until data transfer is complete.
- TCP establishes a reliable connection between sender and receiver using the three-way handshake (SYN, SYN-ACK, ACK).
- Grouping it into segments with headers source and destination port numbers.
- It ensures error-free (Error Checking Mechanisms), in-order delivery of data packets. (Using Segment Numbering)
- Retransmission of lost packets. (Upon No Acknowledgement - Each segment sent must be acknowledged.)
- At the receiver's end, TCP reassembles these segments using sequence numbers.

##### Congestion Control

Controlling how much data is sent through the network at the same time.

**Leaky Bucket Algorithm**:

1. Packets arrive, placed into the bucket (Queue).
2. Bucket leaks (transmits) at a constant rate.
3. If bucket (queue) becomes full, incoming packets are dropped.

**Token Bucket Algorithm**:

1. Tokens are added to the bucket at regular intervals.
2. Each token permits sending one packet.
3. If tokens exist, packets can be transmitted immediately.
4. If no tokens, packets must wait.
5. Handles bursty traffic efficiently without unnecessary data loss.

#### User Datagram Protocol (UDP)

Connectionless Protocol.

- Faster and Lightweight.
- No overhead for opening a connection, maintaining a connection, or terminating a connection.
- It does not guarantee delivery, order, or error checking.
- No acknowledgment. No retransmission of lost packets.
- Suitable for real-time and time-sensitive applications such as video streaming, DNS.

---

### Layer 5: Session Layer

- Provides mechanisms for session setup, management and termination.
- Ensures that communication remains synchronized and reliable, even during long or complex data transfers.
- Handles dialogue control, deciding whose turn it is to send or receive data.

---

### Layer 6: Presentation Layer (Translation Layer)

- Ensures that the data exchanged between devices is in a format both systems can understand.
- Maintains proper syntax and semantics of the data.
- Provides encryption and decryption for secure communication. Prevents Eavesdropping and Man in the middle attack.

#### SSL and TLS Protocols

**SSL (Secure Sockets Layer)** and **TLS (Transport Layer Security)** Protocols:

1. Server sends digital certificate, Client verifies certificate using Certificate Authority (CA)
2. Client and server agree on a shared secret key.

---

### Layer 7: Application Layer

#### HTTP (Hypertext Transfer Protocol)

Set of rules for transferring data web browser and a web server.

- **Stateless** (Uses TCP): Each request is independent and the server doesn't retain previous interactions' information.
- **Request Methods**: GET, POST, PUT, DELETE for different actions on resources.
- **Status Codes**: 
  - 2xx (Success)
  - 4xx (Client Error)
  - 5xx (Server Error)

#### HTTPS (HyperText Transfer Protocol Secure)

Secure variant of HTTP (Adds a layer of SSL/TLS).

#### Domain Name System (DNS)

Translates domain names into IP addresses.

**DNS Resolution Process**:

1. Browser first checks its local cache to see if it already has IP address for the domain.
2. If not, sends a request to a DNS resolver provided by Internet Service Provider (ISP).
3. The resolver sends the request to a root DNS server.
4. DNS server sends this IP address with TTL back to the resolver.
5. DNS resolver sends the IP address to your computer, cache is updated.

#### Remote Procedure Call (RPC)

Enables a program to call a function on another machine as if it were a local function call.

**Process**:

1. Client calls local stub
2. Client stub (proxy): Marshals parameters (Transmittable Format) and Sends request over network
3. Server stub (skeleton): Unmarshals parameters (Original Format) and Calls actual procedure
4. Server executes procedure and Returns Result

**Failure Semantics**:

- **At-most-once**: Procedure executes 0 or 1 time
- **At-least-once**: Procedure executes ≥1 times

#### gRPC (google RPC)

- Data format: Protocol Buffers (binary)
- Language-neutral, binary serialization. Faster and smaller than JSON.
- User defines services and messages (Format) in `.proto` file.
- `protoc` compiler generates: Client stub (proxy) and Server stub (skeleton)
- Generated in multiple languages (Java, Python, Go, C++)

---

## TCP/IP Model

4 Layer Model.

- **Application Layer**: Provides network services directly to end-user applications.
- **Transport Layer**: Responsible for making sure that data is sent reliably and in the correct order. (TCP/UDP)
- **Network Layer**: Responsible for routing data across different networks to destination. (IP)
- **Link Layer**: Responsible for data transfer over a Physical media.

---

## VPN (Virtual Private Network)

- Creates a secure, encrypted tunnel over internet to safely connect users or networks as if they were on a private network. Hides IP.

**Types**:

- **Site-to-Site VPN**: Connects two entire networks (e.g., branch offices) securely over the internet. Cheaper than setting WAN connections.
- **Remote Access VPN**: Lets individuals securely connect to a private network.
