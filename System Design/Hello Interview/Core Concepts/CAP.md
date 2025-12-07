# CAP Theorem

In a distributed system, you can only guarantee 2 out of 3 properties:

---

## The Three Properties

**Consistency:**  
All nodes see the same data at the same time.

**Availability:**  
Every request to a non-failing node receives a response, without the guarantee that it is the most recent data.

**Partition Tolerance:**  
The system continues to operate despite failure of part of the system (i.e., network partitions between nodes).

---

## The Trade-off

In any distributed system, **partition tolerance is a must**. Network failures will happen, and your system needs to handle them.

So it boils down to a single choice: **Do you prioritize consistency or availability?**

---

## Real-World Example

**Scenario:**

- User A connects to their closest server (USA) and updates their name
- This update is replicated to the server in Europe
- When User B in Europe views User A's profile, they see the updated name

**Network Partition Occurs:**  
The connection between USA and Europe servers goes down. Now we have a critical decision to make:

- **Consistency:** Return an error because we can't guarantee the data is up-to-date
- **Availability:** Show potentially stale data

---

## When to Choose Consistency

Use consistency when data accuracy is critical and errors are expensive:

- **Ticket Booking Systems:** Prevent the same seat from being booked twice
- **E-commerce Inventory:** Prevent over-selling out-of-stock items
- **Financial Systems:** Ensure account balances are always accurate

---

## When to Choose Availability

Use availability when eventual consistency is acceptable:

- **Social Media:** Profile picture updates can take a few seconds to propagate
- **Content Platforms (Netflix):** Movie descriptions can be slightly out-of-date momentarily
- **Review Sites (Yelp):** Working hours can take time to update across all servers

---

## Design Patterns by Choice

### If You Prioritize Consistency

Your design might include:

**Distributed Transactions:**  
Ensuring multiple stores (like cache and DB) remain in sync through **2PC (Two-Phase Commit)**.  
Downside: Higher latency due to coordination overhead.

**Single-Node Solutions:**  
Using a single DB instance to avoid replication issues entirely.  
Choices: PostgreSQL, MySQL

---

### If You Prioritize Availability

Your design can include:

**Multiple Replicas:**  
Scaling to additional read replicas with **asynchronous replication**, allowing reads to be served from any replica even if it's slightly behind.

**Change Data Capture (CDC):**  
Using CDC to track changes in the primary DB and propagate them **asynchronously** to replicas and caches.

Choices: Redis, DynamoDB, Cassandra

---

## Important Note

**Real-world systems frequently need both availability and consistency for different features.**

When discussing non-functional requirements, **CAP theorem should be your starting point**.

Different parts of your system can make different choices:

- Financial transactions: Prioritize consistency
- User feeds: Prioritize availability
- Both coexist in the same application