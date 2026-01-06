# Networking — Core Concepts

Networks are built on a layered architecture (the so-called "OSI model")

## 7 OSI Layers
- Application Layer (7)  
- Presentation Layer  
- Session Layer  
- Transport Layer (4)  
- Network Layer (3)  
- Data Link Layer  
- Physical Layer

---

## Network Layer (3)

At this layer, IP protocol handles routing and addressing.  
In a system, nodes are assigned IPs usually by a DHCP server when they boot up.  
We can create a private network with many servers and give them any IP address we want, but if you want internet traffic to be able to find you'll need to use public IP addresses that are routable and allocated by a RIR (Regional Interest Registry); are used to identify devices on the internet.

IP is responsible for:
- breaking the data into packets,
- handling packet forwarding between networks, and
- providing best-effort delivery to any destination IP address on the network.

---

## Transport Layer (4)

The transport layer is where we establish end-to-end communication between devices.  
At this layer, we have TCP and UDP, which provide end-to-end communication services. Provides features like reliability, ordering, and flow control on top of the network layer.

### UDP (User Datagram Protocol): Fast but Unreliable = Spray and Pray
- Connectionless: No handshake or connection setup  
- No guarantee of delivery: Packets may be lost without notification  
- No ordering: Packets may arrive in a different order than sent  
- Lower latency: Less overhead means faster transmission  
- Only visible: the source IP address and port and where the destination IP address and port.

Usage:
- You might choose UDP when:
  - Low latency is critical (real-time applications, video streaming, gaming)
  - Some data loss is acceptable (media streaming)
  - You don't need to support web browsers (or you have an alternative for that client)

### TCP (Transmission Control Protocol): Reliable but with Overhead
- Connection-oriented: Establishes a dedicated connection before data transfer  
- Reliable delivery: Guarantees that data arrives in order and without errors  
- Flow control: Prevents overwhelming receivers with too much data  
- Congestion control: Adapts to network congestion to prevent collapse

This connection is called a "stream" and is a stateful connection between the client and server. TCP will ensure that recipients of messages acknowledge their receipt and, if they don't, will retransmit the message until it is acknowledged.

Usage:
- TCP is ideal for applications where data integrity is critical

### Feature Comparison

| Feature | UDP | TCP |
|---|---:|---:|
| Connection | Connectionless | Connection-oriented |
| Reliability | Best-effort delivery | Guaranteed delivery |
| Ordering | No ordering guarantees | Maintains order |
| Flow Control | No | Yes |
| Congestion Control | No | Yes |
| Header Size | 8 bytes | 20–60 bytes |
| Speed | Faster | Slower due to overhead |
| Use Cases | Streaming, gaming, VoIP | Everything Else |

---

## Application Layer (Layer 7)

At the final layer are the application protocols like DNS, HTTP, Websockets, WebRTC. These are common protocols that build on top of TCP (or UDP, in the case of WebRTC) to provide a layer of abstraction typically associated with web applications.

### HTTP/HTTPS — Hypertext Transfer Protocol (HTTP): The Web's Foundation

- HTTP is a stateless protocol, meaning that each request is independent. The server doesn't need to maintain any information about previous requests.

You'll see a few key concepts:
- Request methods: GET (Idempotent), POST (Create), PUT (Update), DELETE (Idempotent)  
- Status codes: 200 OK, 404 Not Found, 401 Unauthorised (Requires Auth), 403 Forbidden (Auth Refused), 500 Server Error, 502 Bad Gateway  
- Headers: Metadata about the request or response  
- Body: The actual content being transferred

The HTTP `Accept-Encoding` header provides clients a way to indicate they can handle different types of content encoding. Servers can then respond with the most efficient encoding for that client with `Content-Encoding: X`, providing both backward compatibility and graceful degradation.

HTTPS adds a security layer (TLS/SSL) to encrypt communications, protecting against eavesdropping and man-in-the-middle attacks.  
- TLS = Transport Layer Security  
- SSL = Secure Sockets Layer

---

## What happens when you type (e.g.) hellointerview.com into your browser and press enter?

1. DNS Resolution:  
   The client starts by resolving the domain name of the website to an IP address using DNS (Domain Name System).

2. TCP Handshake:  
   The client initiates a TCP connection with the server using a three-way handshake:
   - SYN: The client sends a SYN (synchronize) packet to the server to request a connection.
   - SYN-ACK: The server responds with a SYN-ACK (synchronize-acknowledge) packet to acknowledge the request.
   - ACK: The client sends an ACK (acknowledge) packet to establish the connection.

3. HTTP Request:  
   Once the TCP connection is established, the client sends an HTTP request to the server to request the page.

4. Server Processing:  
   The server processes the request, retrieves the requested web page, and prepares an HTTP response.

5. HTTP Response:  
   The server sends the HTTP response back to the client, which includes the requested web page content.

6. TCP Teardown:  
   After the data transfer is complete, the client and server close the TCP connection using a four-way handshake:
   - FIN: The client sends a FIN (finish) packet to the server to terminate the connection.
   - ACK: The server acknowledges the FIN packet with an ACK.
   - FIN: The server sends a FIN packet to the client to terminate its side of the connection.
   - ACK: The client acknowledges the server's FIN packet with an ACK.

The connection between the client and server is a state that both the client and server must maintain. We need to repeat this connection setup process for every request - a potentially significant overhead. The higher in the stack we go, the more latency and processing required.


## APIs: Communication Between Services

Communication between services is generally via **APIs**. For creating these APIs, there are three main paradigms:

1. **REST**
2. **GraphQL**
3. **gRPC**

---

### REST API — Representational State Transfer

**Core Principle:**
Clients perform simple operations against **resources**. RESTful APIs use HTTP methods together with opinionated conventions about paths and request bodies, and often use JSON to represent resources in both request and response bodies.

**Key Concept:**
- ❌ **Not RESTful:** `POST /updateUser` (operation-focused)
- ✅ **RESTful:** `PUT /users/{id}` (resource-focused)

In REST, we think in terms of resources and the operations we can perform on them.

**Performance Considerations:**
- REST is not the most performant solution for very high throughput services
- JSON is an inefficient format for serializing and deserializing data

---

### GraphQL

**Core Principle:**
GraphQL allows clients to request **exactly the data they need**.

**Problems It Solves:**

**Under-Fetching:**
A page requires many API calls to render, resulting in inefficient data retrieval.

**Over-Fetching:**
API responses contain far more data than needed to guard against future use-cases.

**How It Works:**
GraphQL specifies which fields and nested objects to fetch. The backend interprets this query and responds with just the data the frontend needs.

**Important Consideration:**
Execution of GraphQL queries can be a source of latency and complexity for the backend.

**Best Use Cases:**
- Frontend team needs to iterate quickly
- Requirements change frequently
- Apps need to adapt quickly to changing requirements

---

### gRPC — Google Remote Procedure Call

**Core Principle:**
Binary encoding instead of JSON — faster and more efficient than JSON over HTTP.

**Technical Details:**
- Uses very skinny tags and variable-length encoding of strings
- Requires less space and less CPU to parse
- Builds on protocol buffers to provide strong typing
- Strong typing helps catch errors at compile time rather than runtime

**Architecture:**
gRPC shines in **microservices architectures** where services need to communicate efficiently.

**When to Use:**
- Internal service-to-service communication
- Performance is critical
- Latencies are dominated by the network rather than server work

---

## Server-Sent Events (SSE)

**Concept:**
SSE is a technique built on top of HTTP that allows a server to stream multiple messages over time in a single response.

**How It Works:**
- One continuous HTTP response (same TCP connection)
- Response comes in over many smaller chunks
- Clients process each line of the body individually to react to data as it arrives

**Connection Limitation:**
SSE connections cannot remain open indefinitely because servers, load balancers, or proxies will close them.

**Automatic Reconnection:**
The SSE standard defines the behavior of an **EventSource object** that, once the connection is closed, will automatically reconnect with the ID of the last message received.

---

## WebSockets

**Concept:**
Many applications need **real-time bidirectional communication**. WebSockets provide a persistent, TCP-style connection between client and server with broad support.

**Key Features:**
- Servers can push data to clients without being prompted
- Clients can push data back to the server without waiting

**Connection Flow:**

1. Client initiates **WebSocket handshake over HTTP** (with backing TCP connection)
2. Connection upgrades to **WebSocket protocol**
3. WebSocket takes over the TCP connection
4. Both client and server can send **binary messages** to each other
5. Connection stays open until explicitly closed

**Data Format:**
Use **JSON** to define what client and server are receiving.

**Best For:**
Real-time applications, games, and live updates.

---

## WebRTC

**Concept:**
WebRTC is the **only application-level protocol that uses UDP**. It enables **direct peer-to-peer communication** between browsers without requiring an intermediary server for data exchange.

**Connection Process:**

1. Clients connect to a **central signaling server** to learn about their peers
2. Clients reach out to a **STUN server** to get their public IP address and port
3. Clients share this information with each other via the signaling server
4. Clients establish a **direct peer-to-peer connection** and start sending data
5. If connection fails, fallback to a **TURN server**

**Ideal For:**
Audio/video calling and conferencing applications.

---

## Load Balancing

**Problem:**
How to distribute incoming requests across multiple servers to improve performance and reliability.

**Scaling Options:**
- **Vertical Scaling:** Use bigger, more powerful servers
- **Horizontal Scaling:** Add more servers

---

### Client-Side Load Balancing

**Concept:**
The **client decides which server** to talk to.

**How It Works:**
- Client makes a request to a service registry or directory containing available servers
- Client periodically polls or receives push updates when servers change

**Example: DNS**
When you request a domain like `example.com`, your DNS resolver returns a rotated list of IP addresses. Each new request gets a different ordering, effectively doing client-side load balancing.

**Advantages:**
- Avoids a single point of failure
- Can use two load balancers and rotate between them via DNS

**When to Use:**
- Small number of clients that you control
- Large number of clients but can tolerate slow updates (periodic polling)

**Limitations:**
- Update time scales with the number of clients to notify
- DNS entries have a **TTL (Time To Live)** — updates cannot be faster than the TTL

---

### Dedicated Load Balancers

A **server or hardware device** that sits between clients and backend servers, making intelligent routing decisions.

---

#### Layer 4 Load Balancers (Transport Layer)

**Example:** AWS Network Load Balancer (NLB)

**How It Works:**
- Operate at the **transport layer (TCP/UDP)**
- Make routing decisions based on network information (IP addresses, ports)
- **Do NOT examine** the actual content of packets

**Characteristics:**
- Maintain persistent TCP connections between client and server
- Fast and efficient due to minimal packet inspection
- Cannot make routing decisions based on application data
- Typically used when raw performance is the priority

**Connection Persistence:**
If a client establishes a TCP connection through an L4 load balancer, that **same server handles all subsequent requests** within that session.

**When to Use:**
Great for WebSocket connections and other protocols requiring persistent connections.

---

#### Layer 7 Load Balancers (Application Layer)

**Example:** AWS Application Load Balancer (ALB)

**How It Works:**
- Operate at the **application layer**, understanding protocols like HTTP
- Examine the actual content of each request
- Make intelligent routing decisions based on application data

**Characteristics:**
- Terminate incoming connections and create new ones to backend servers
- Route based on request content (URL, headers, cookies, etc.)
- More CPU-intensive due to packet inspection
- Better suited for HTTP-based traffic

**Advanced Routing:**
An L7 load balancer could route all API requests to one set of servers while sending web page requests to another (simulating an API Gateway).

**When to Use:**
Great for HTTP-based traffic.

---

### Health Checks and Fault Tolerance

**Purpose:**
Determine if a server is healthy and able to handle requests.

**How It Works:**
- If a server crashes or loses power, the load balancer stops routing traffic to it
- Health checks run at configurable intervals using different protocols

**Types of Health Checks:**

**TCP Health Check:**
- Simple and efficient way to check if server accepts new connections

**Layer 7 Health Check:**
- Makes an HTTP request to the server
- Ensures the response is successful

---

### Load Balancing Algorithms

| Algorithm | Description |
|-----------|-------------|
| **Round Robin** | Requests distributed sequentially across servers |
| **Random** | Requests distributed randomly across servers |
| **Least Connections** | Requests go to server with fewest active connections |
| **Least Response Time** | Requests go to server with least response time |
| **IP Hash** | Client IP determines which server gets request (for session persistence) |

**Best Practice:**
Round robin or random algorithms are appropriate, especially for stateless applications.

---

## Regionalization and Latency

### Global Deployment

**Structure:**
- Servers distributed across the world
- Multiple data centers in a single region (Amazon calls these **"availability zones"**)

**Key Principle:**
The physical distance between clients and servers significantly impacts network latency.

**Data Locality:**
Data is kept as close as possible to the computations that need to access it.

---

### Content Delivery Network (CDN)

**Concept:**
Networks of servers strategically located around the world at **"edge locations."**

**How It Works:**
- If an edge server can answer a user's request, the user gets a lightning-fast response
- Effectiveness depends on **caching**
- Ideal for static content like images and videos

**When to Use:**
Data that is highly cacheable and needs to be queried from across the globe.

---

### Regional Partitioning

**Example:** Uber

**Concept:**
Partition data by region so each region contains only relevant data.

**Structure:**
- Each region has its own database
- Servers handling requests are co-located with their databases

**Performance Benefits:**
- Regional services answer queries quickly (low latency)
- Local database access is very fast

---

## Handling Failures

---

### Timeout and Retries

**Concept:**
Set a timeout for expected request duration. If exceeded, retry the request.

**Key Requirement:**
**Idempotent APIs** are essential because requests can be retried multiple times without causing issues.

---

### Backoff

**Concept:**
Instead of retrying immediately, wait before retrying. If it fails again, wait longer.

**Benefits:**
- Gives the system time to recover
- Reduces load on struggling systems

---

### Jitter

**Concept:**
Add randomness to the backoff strategy.

**Why It Matters:**
Coordinated retries from all clients at the same time create thundering herd problems. Jitter spreads retry attempts over time.

---

### Idempotency

**Definition:**
Idempotent APIs can be called multiple times and produce the same result every time.

**Implementation:**
Use an **idempotency key** — a unique identifier for a request ensuring the same request is idempotent.

**Example Use Case:**
Payment systems (ensure a payment is processed exactly once, even if the request is retried).

---

### Cascading Failures and Circuit Breakers

**Cascading Failures:**
Scenarios where one failure creates new failures downstream, potentially crashing the entire system.

**Circuit Breaker Pattern:**
A protective mechanism when network calls to dependencies fail repeatedly.

**How It Works:**

1. **Monitor failures** when calling external services
2. **Trip the circuit** to an **open state** when failures exceed a threshold
3. **Fail fast** — while open, requests immediately fail without attempting the call
4. **Transition to half-open** after a timeout period
5. **Test request** determines whether to close or keep open

**Advantages:**

- **Reduce Load:** Prevent overwhelming struggling services with more requests
- **Improved UX:** Provide fast fallbacks instead of hanging UI

**When to Use:**
- External API calls to third-party services
- Database connections and queries
- Service-to-service communication in microservices