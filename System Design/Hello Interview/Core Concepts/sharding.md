# Sharding

When a single database can't keep up anymore (high storage size or high read/write ops), split your data across multiple machines.

---

## Partitioning vs Sharding

**Partitioning:** Usually refers to splitting data within a single database instance, often by table ranges or hash partitions. Organizes data so the database can work more efficiently (efficient queries).

**Types of Partitioning:**

- **Horizontal Partitioning:** Split rows across partitions
- **Vertical Partitioning:** Split columns across partitions (same rows, fewer columns per partition)

**Sharding:** Means splitting data across multiple machines. Each shard holds a subset of the data, and together the shards make up the full dataset. Each shard is a standalone database with its own CPU, memory, storage, and connection pool.

---

## How to Shard

### What to Shard By

The field or column you use to split the data. It defines how the data is grouped.

### How to Distribute It

The rule for assigning those groups to shards. It defines how the data is distributed across machines.

**Bad Shard Key Problems:**

- Uneven data distribution
- Hot spots where one shard gets pounded while others sit idle
- Queries that have to hit every shard to find what they need

### Good Shard Key Characteristics

- **High Cardinality:** The key should have many unique values (not a boolean field)
- **Even Distribution:** Values should spread evenly across shards
- **Aligns with Queries:** Your most common queries should ideally hit just one shard

**Examples:**

- `user_id` for user-centric apps
- `order_id` for e-commerce orders table

---

## Sharding Strategies

### Range-Based Sharding

Groups records by a continuous range of values, then assigns value ranges to shards.

**Example:**

- Shard 1 → User IDs 1–1M
- Shard 2 → User IDs 1M–2M

---

### Hash-Based Sharding (Default)

Uses a hash function to evenly distribute records across shards.

**How It Works:**

``` 
shard = hash(user_id) % 4
```

**Advantages:**

- Even distribution
- New users get distributed evenly

**Disadvantage:** When you need to add or remove shards, you have to reshuffle massive amounts of data.

**Solution: Consistent Hashing** Hash, move clockwise to nearest shard (minimizes reshuffling).

---

### Directory-Based Sharding

Uses a lookup table to decide where each record lives.

**Advantages:**

- Can implement complex sharding logic that would be impossible with a simple hash function

**Disadvantages:**

- Every single request requires a lookup (adds latency)
- Single Point of Failure: If the directory goes down, your entire system stops working even though shards are healthy

---

## Challenges of Sharding

### Hot Spots and Load Imbalance

Even with a good shard key, some shards can end up handling way more traffic than others. This is called a **hot spot** and negates the purpose of sharding.

**Handling Strategies:**

**Isolate Hot Keys:** Dedicate powerful shards to hot keys.

**Compound Shard Keys:** Instead of sharding just by `user_id`, combine it with another dimension like `hash(user_id + date)`. This spreads a single user's data across multiple shards over time.

**Dynamic Shard Splitting:** Some databases support automatically splitting a shard when it gets too large or too hot.

---

### Cross-Shard Operations

Instead of querying one database, you have to query multiple shards, wait for all of them to respond, and aggregate the results yourself.

**Minimizing Cross-Shard Queries:**

**Cache the Results:** If eventual consistency is acceptable, cache aggregated results.

**Denormalize to Keep Related Data Together:** Duplicate data to let you query everything from one shard (more complex updates, but fewer cross-shard queries).

**Accept the Hit for Rare Queries:** Okay as long as it's infrequent.

---

### Maintaining Consistency

Sharding breaks consistency because you're coordinating writes across multiple DBs that don't know about each other.

**Handling Strategies:**

**Design to Avoid Cross-Shard Transactions:** Structure your data and queries to minimize multi-shard operations.

**Use Sagas for Multi-Shard Operations:** Break the operation into a sequence of independent steps, each with a compensating action. This gives you eventual consistency.

**Example:**

1. Deduct money from User A's account (shard 1)
2. Add money to User B's account (shard 2)
3. If step 2 fails, refund User A (compensating action)

**Accept Eventual Consistency:** For many operations, strict consistency isn't required.