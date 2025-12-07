## Data Modeling:
It is the process of defining how your application’s data is structured, stored, and related

## Database Models:

### Relational Databases (SQL):
Relational databases organize data into tables with fixed schemas, where rows represent entities and columns represent attributes.
They enforce relationships through foreign keys and provide ACID guarantees for transactions; constraints and foreign keys preserve integrity.

When strong consistency is a non-functional requirement, like ensuring payments don't double-charge or inventory doesn't oversell, SQL's ACID guarantees are the right tool for the job.

Modern SQL databases scale with techniques like read replicas, sharding, connection pooling, and caching.  
Ex: PostgreSQL

---

### Document Databases:
Stores data as JSON-like documents with flexible schemas, making them good for rapidly evolving applications where you don't know all your data fields upfront. 

Nesting and embedding related information within documents rather than normalizing across tables.  
This eliminates Joins.

This trades storage space and update complexity for read performance.  
Ex: MongoDB

---

### Key-Value Stores
Provide simple lookups where you fetch values by exact key match. They're extremely fast but offer limited query capabilities beyond that basic operation.

Used:  
For caching, session storage, feature flags, or any scenario where you only need to look up data by a single identifier. 

Usually, SQL as your source of truth with a key-value cache (like Redis) in front for hot data. This is great for reads but terrible for consistency when data changes.  
EX: Redis, DynamoDB

---

### Graph Databases:
Entities as nodes, and relationships through edges.  
Ex: Neo4j

---

### Keys:
Each entity needs a primary key to identify individual records. 
Use system-generated IDs like user_id or post_id rather than business data like email addresses.

These relationships are enforced through foreign keys in SQL or by application logic in NoSQL.  
Foreign keys help ensure referential integrity - Prevent orphaned records; like a post referencing a user that doesn't exist.

However, they come at a cost because the database has to validate each insert/update. At very large scale, some companies drop them for write performance and enforce integrity at the application level.

Constraints like NOT NULL, UNIQUE, enforce correctness at the database level. They protect data quality.

---

## Indexing:
Indexes are data structures that help the database find records quickly without scanning every row.  
Indexes should directly support your most important queries.  
Ex: Index on posts.user_id to quickly find all posts by a user.  
The GET /users/{id}/posts endpoint needs the above index.

---

## Normalization:
Normalization means storing each piece of information in exactly one place. User data lives only in the users table, not duplicated across other tables. This prevents data anomalies where updates happen in one place but not another, leading to inconsistent state.

Start with a clean normalized model and denormalize only when needed. Avoid repeating data in your schema design.  
Put a cache in front that has a denormalized representation of the data. Your source of truth stays clean and normalized, but your cache can have pre-computed joins, aggregations.

Denormalisation usage: Analytics and reporting systems, Event logs and audit trails where you're capturing a snapshot of data at a point in time, Heavily read-optimized systems.

---

## Scaling and Sharding
When your data gets too large for a single database, you need to shard it across multiple machines.  
keep related data together. Shard by the primary access pattern  
Avoid cross-shard queries whenever possible.

---

## Ex: Database (Postgres)

**Posts**
- postId (pk, shard)
- userId (fk, index)
- content
- mediaUrls
- createdAt (index)

**Users**
- userId (pk)
- name
- email (unique)
- createdAt

**Comments**
- commentId (pk)
- postId (fk, index, shard)
- userId (fk, index)
- content 
- createdAt (index)