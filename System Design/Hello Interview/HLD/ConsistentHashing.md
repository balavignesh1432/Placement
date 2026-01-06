# Consistent Hashing

## Modulo Hashing

The most straightforward approach to distribute data across multiple databases is modulo hashing.

**How It Works:**
1. Take the event ID and run it through a hash function
2. Perform the modulo operation (%) with the number of databases
3. The result tells us which database should store that event

**The Problem:**
When you want to add a fourth database instance, most of the data needs to be redistributed, causing huge spikes in DB load.

Same problem occurs when a DB instance is removed or goes down.

---

## Consistent Hashing

Arrange databases in a circular space, often called a **"hash ring."**

**How It Works:**

1. Create a hash ring with a fixed number of points (usually INT size, 2^32 - 1)
2. Place DBs evenly around the ring (If 100 points and 4 DBs, then at positions 0, 25, 50, 75)
3. Hash the eventID to get an INT hash
4. Find that value on the ring and move clockwise until a DB is found

**Adding a New Database:**
If we add a 5th DB at position 90 on our ring:
- Only events that hashed to positions between 75 and 90 (previously went to DB at 75) need to move to the new DB
- All other events stay exactly where they are

**Removing a Database:**
Similar limited movement occurs when removing a DB instance (Say DB2).

**The Trade-off:**
Now DB 3 has 2x the load of DB 1 and DB 4 (uneven distribution).

---

## Virtual Nodes

Instead of putting each DB at just one point on the ring, we put it at **multiple points**.

**How It Works:**

Hash multiple virtual nodes per database:
- `"DB1-vn1"` → position 15
- `"DB1-vn2"` → position 25
- `"DB1-vn3"` → position 40

**When Database 2 Fails:**
- Events mapped to `"DB2-vn1"` redistribute to Database 1
- Events mapped to `"DB2-vn2"` go to Database 3
- Events mapped to `"DB2-vn3"` go to Database 4
- And so on...

**Benefit:**
The load from the failed database gets distributed much more evenly across all remaining databases instead of overwhelming just one neighbor.

**Tuning:**
The more virtual nodes you use per database, the more evenly distributed the load becomes.

---

## General Applications

Consistent hashing can be applied to any scenario where distribution is needed:

- **Databases** — Distribute data across DB shards
- **Caches** — Distribute cache across Redis nodes
- **Message Brokers** — Distribute messages across broker instances
- **Servers** — Distribute requests across server clusters