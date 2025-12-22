## Database Basics

- **Database**: Collection of data.

- **File-based System**  
  - Data is stored in flat files without any relationship between data.  
  - No indexing → super slow retrieval.  
  - Data redundancy is common.  
  - No concurrency control.

- **Database Management System (DBMS)**  
  - Software used to manage and organize databases.  
  - Handles storing, retrieving, and updating data.  
  - Ensures **data integrity**, **security**, and manages **concurrency**.  
  - **Data Security**: Provides controlled access to sensitive data (e.g., RBAC and encryption mechanisms).  
  - **Data Integrity**: Ensures that the data is accurate and consistent.  
  - **Efficient Data Retrieval**: Optimizes queries and indexing.

- **Data Warehousing**  
  - Process of collecting, extracting, transforming, and loading data from multiple sources.  
  - Stores data in one central database or repository (data warehouse).

### DBMS Architectures

- **2-tier Architecture (Client–Server)**  
  - Applications at the client end directly communicate with the database at the server end without any middleware.  
  - **Pros**: Faster.  
  - **Cons**: Less secure and not scalable.  
  - **Example**: Library Management System.

- **3-tier Architecture**  
  - The client does not directly communicate with the database.  
  - Client → Application Server → Database System.  
  - **Pros**: Scalable and secure.  
  - **Cons**: Added latency and higher maintenance.  
  - **Example**: E‑commerce store.


## Components of a DBMS

- **Database Schema**:  
  Defines the structure and organization of the database (tables, attributes, constraints, relationships).

- **Query Processor**:  
  Interprets and executes SQL queries.

- **Transaction Manager**:  
  Ensures the ACID properties of transactions.

- **Storage Manager**:  
  Manages the physical storage of data.


### Phases of Query Processing

1. **Parsing**:  
   - The SQL query is parsed to check its syntax and semantics (against the schema).
2. **Translation**:  
   - The query is translated into an internal form, such as an execution plan.
3. **Optimization**:  
   - The query is optimized to determine the most efficient execution plan, considering factors like indexes and joins.
4. **Execution**:  
   - The optimized query plan is executed by the query processor, and results are returned.


### Intension vs Extension

- **Intension (Database Schema)**:  
  Defines the structure of the database.

- **Extension (Snapshot)**:  
  Number of tuples (records) present in the database at any given point in time.


## Relational DBMS (RDBMS) and Relations

- **Relational DBMS (RDBMS)**:  
  Data is organized in tables (relations) and managed through SQL.  
  **Examples**: MySQL, PostgreSQL.

- **Relation (Table) in DBMS**:  
  - A relation is a table that consists of rows and columns.  
  - Each row represents a **tuple/record**.  
  - Each column represents an **attribute/property** of the entity.  
  - Relations are defined by a **schema**, which specifies the attributes (columns) of the table.


### Keys in RDBMS

- **Super Key**:  
  A set of one or more attributes (columns) that can uniquely identify a tuple (row) in a table.

- **Candidate Key**:  
  A minimal super key that uniquely identifies a tuple in a relation (no proper subset of it is a super key).

- **Primary Key**:  
  - A chosen candidate key that acts as the unique identifier for each record in a table.  
  - **Cannot contain NULL values**.  
  - A relation can have multiple candidate keys, and exactly one of them is chosen as the primary key.

- **Foreign Key**:  
  An attribute that links to the primary key (or a unique key) in another table.  
  It creates a relationship between two tables and ensures **referential integrity**.


### Data Redundancy and Constraints

- **Data Redundancy**:  
  Unnecessary repetition of data in a database. It can lead to:  
  - Inconsistencies  
  - Increased storage requirements  
  - Maintenance challenges

- **Reduction Methods**:  
  - **Normalization**  
  - **Using Constraints**

- **Constraints in DBMS**:  
  Rules that limit the type of data that can be inserted into a table to ensure data integrity and consistency.  
  - **NOT NULL**: Column cannot store NULL values.  
  - **UNIQUE**: All values in a column must be unique.  
  - **PRIMARY KEY**: Combines NOT NULL + UNIQUE, and uniquely identifies each row.  
  - **FOREIGN KEY**: Maintains referential integrity between tables.  
  - **CHECK**: Ensures that values in a column satisfy a specific condition.  
  - **DEFAULT**: Assigns a default value to a column if no value is provided.

- **Referential Integrity**:  
  - The foreign key in one table must match a primary key or a unique key in another table.  
  - Ensures there are no **orphan records** in the database.


## Normalization and Denormalization

- **Normalization**:  
  Organizing data in a way that reduces redundancy and prevents anomalies.  
  Involves dividing large tables into smaller ones and defining relationships between them to ensure data integrity.

### Normal Forms

- **1NF (First Normal Form)**  
  - Each column contains **atomic (indivisible)** values.  
  - Each record (row) is unique.  
  - Often achieved by splitting one row into multiple rows to remove repeating groups.

- **2NF (Second Normal Form)**  
  - Table must already be in **1NF**.  
  - All non-key attributes (attributes other than the candidate key) must be **fully functionally dependent** on the primary key.  
  - No **partial dependencies** on a part of a composite primary key.  
  - If partial dependencies exist, split columns into separate tables, where the partially dependent attribute becomes part of a new primary key, and the columns that were partially dependent on it become fully dependent in the new table.

- **3NF (Third Normal Form)**  
  - Table must already be in **2NF**.  
  - No **transitive dependencies** between non-key attributes.  
  - For a functional dependency \( X \rightarrow Y \):  
    - Either \( X \) must be a **super key**, or  
    - \( Y \) must be part of a **super key**.  
  - If transitive dependencies exist, split columns into separate tables.

- **Boyce–Codd Normal Form (BCNF)**  
  - A stricter version of 3NF.  
  - For **every** functional dependency \( X \rightarrow Y \), \( X \) **must be a super key**.  
  - The left side of every dependency must be able to uniquely identify the entire row.

- **Denormalization**:  
  - The process of **combining tables** to improve query performance.  
  - Often introduces **controlled redundancy**.  
  - Mainly used to improve speed for **read-heavy** operations.


## Levels of Abstraction in DBMS

- **Physical Level**  
  - Deals with **how data is physically stored in memory**.  
  - Includes file organization techniques (e.g., **indexing**, **hashing**) and access methods (random or sequential).  
  - These details are typically hidden from system administrators, developers, and users.

- **Conceptual (Logical) Level**  
  - Deals with **what data is stored** in the database and **what relationships** exist between data.  
  - This is the level on which developers and system administrators usually work.

- **External (View) Level**  
  - Deals with **only part of the database**, providing different views of the same data for different users.  
  - Access is typically through a **GUI** or **CLI**.


### Data Independence

- **Data Independence**:  
  Property that allows changes at one level of the database architecture without requiring changes at higher levels.

- **Physical Data Independence**:  
  - Ability to change the **physical storage** of data without affecting the **logical schema**.  
  - **Examples**:  
    - Changing from sequential file organization to hashing.  
    - Using a new storage device.

- **Logical Data Independence**:  
  - Ability to modify the **logical schema** without affecting user views or application programs.  
  - **Examples**:  
    - Adding new fields or modifying relationships in the conceptual schema.


### Views

- **View**:  
  - A **virtual table** created by querying one or more base tables.  
  - Does **not** store data physically.  
  - Presents data from other tables.

- **Materialized View**:  
  - A database object that **contains the results of a query**.  
  - Unlike a regular view, it **stores data physically**.  
  - Improves query performance by **precomputing and storing results**.


## Cursors, Relationships, and ER Diagrams

- **Cursor in DBMS**:  
  - A **pointer** to a result set of a query.  
  - Allows for **row-by-row processing** of query results.  
  - Useful when dealing with large datasets.
  - **Implicit Cursors**: Automatically created by the DBMS.  
  - **Explicit Cursors**: Manually created and controlled by the programmer.


### Types of Relationships

- **One-to-One (1:1)**:  
  A record in one table is associated with a single record in another table.

- **One-to-Many (1:M)**:  
  A record in one table is associated with **multiple** records in another table.

- **Many-to-Many (M:M)**:  
  Multiple records in one table are associated with **multiple** records in another table.


### Entity–Relationship Diagram (ERD)

- **ERD**:  
  A visual representation of the **entities** within a system and the **relationships** between those entities.

- **Entities**:  
  Objects or things within the system (e.g., **Student**, **Course**).

- **Attributes**:  
  Properties or details about an entity (e.g., **Student Name**, **Course Duration**).

- **Relationships**:  
  How entities interact with each other (e.g., **Student enrolls in Course**).


## Indexing

- **Index**:  
  A data structure that improves the **speed of data retrieval**.  
  Allows the database to quickly find the location of a record based on one or more column values (the index key).

### B-Tree and B+ Tree

- **B-Tree**:  
  - Maintains **sorted data**.  
  - Supports searches, insertions, and deletions in **logarithmic time** (O(log N)).  
  - Stores data in **both internal and leaf nodes**.

- **B+ Tree**:  
  - An extension of the B-tree and **widely used** in databases for indexing.  
  - Stores **data only in the leaf nodes** (which form a **linked list**).  
  - Internal nodes are used **only for indexing**.

### Types of Indexes

- **Single-column Index**:  
  Created on **one** column.

- **Composite Index**:  
  Created on **multiple** columns.

- **Unique Index**:  
  Ensures that **no two rows** have the same values in the indexed column(s).


## Transactions and ACID Properties

- **Transaction**:  
  A sequence of one or more database operations executed as a **single unit of work**.

### ACID Properties

- **Atomicity**:  
  - All operations in a transaction are treated as a **single unit**.  
  - If **one operation fails**, the entire transaction fails and the database state **remains unchanged**.

- **Consistency**:  
  - Ensures the database starts and ends in a **consistent state**.  
  - All rules, constraints, and integrity conditions are enforced.

- **Isolation**:  
  - Transactions are executed **independently**.  
  - One transaction does **not interfere** with another.

- **Durability**:  
  - Once a transaction is **committed**, its changes are **permanent**, even if a system failure occurs afterward.


### Stored Procedures, Triggers, and Transaction Logs

- **Stored Procedure**:  
  - A precompiled collection of one or more SQL statements stored in the database.  
  - Allows users to execute a series of operations as a **single unit**, improving **performance** and **reusability**.  
  - Can accept **input parameters**, perform operations, and **return results**.

- **Trigger**:  
  - A special kind of stored procedure that **automatically executes** in response to certain events on a table (such as **INSERT**, **UPDATE**, or **DELETE**).  
  - Used to **enforce rules**, **maintain logs**, or ensure **consistency**.

- **Transaction Log**:  
  - A record that keeps track of **all transactions** executed on a database.  
  - In case of a system failure, the log can be used to **recover** the database to its **last consistent state**.


## Data Partitioning

- **Data Partitioning**:  
  Dividing large datasets into smaller, more manageable **partitions** to improve **performance**, **scalability**, and **availability**.

### Types of Partitioning

- **Horizontal Partitioning**:  
  Divides data **by rows** (e.g., split table by ranges of primary keys or by region).

- **Vertical Partitioning**:  
  Divides data **by columns** (different sets of columns stored in different tables/partitions).

- **Range Partitioning**:  
  Data is divided based on a **range of values** of an attribute (e.g., dates, numeric ranges).

- **Hash Partitioning**:  
  - Data is distributed across partitions based on a **hash value** derived from a key column.  
  - A **hash function** takes the key and calculates a hash value, which determines the **bucket or slot** where the data is stored.


## Concurrency Control

- **Concurrency Control**:  
  Ensures that multiple transactions are executed in a way that **prevents conflicts** and maintains **data consistency**.

### 1. Locking

- **Locks**:  
  Mechanism to ensure data consistency when multiple transactions are involved.

- **Shared Lock (S Lock)**:  
  - Allows **multiple transactions** to **read** a resource.  
  - Prevents any transaction from **modifying** that resource while the lock is held.

- **Exclusive Lock (X Lock)**:  
  - Allows a transaction to **read and modify** a resource.  
  - Prevents any other transaction from **reading or modifying** the locked resource.


### Two-Phase Locking (2PL)

- **Two-Phase Locking (2PL)**:  
  - Protocol that governs how locks are **acquired and released**.  
  - Has two phases:  
    1. **Growing Phase**: Transactions **acquire locks** and **cannot release** any lock.  
    2. **Shrinking Phase**: Transactions **release locks** and **cannot acquire** any new lock.  
  - 2PL guarantees **conflict serializability** and ensures **database consistency**, but it does **not prevent deadlocks**.

#### Types of 2PL

- **Basic 2PL**:  
  Locks can be **released before commit** (once the shrinking phase starts).

- **Strict 2PL**:  
  - **Exclusive (X) locks** are held until **commit/abort**.  
  - Prevents **cascading aborts**.

- **Rigorous 2PL**:  
  - Both **S** (shared) and **X** (exclusive) locks are held until **commit/abort**.  
  - Stronger isolation than strict 2PL.

- **Cascading Aborts**:  
  Occur when one transaction aborts and forces other dependent transactions to abort, because they have **read uncommitted (dirty)** data written by it.

- **Dirty Read**:  
  Reading data written by an **uncommitted** transaction.

### 2. Timestamp Ordering:  
  - Each transaction is assigned a unique **timestamp**.  
  - The system uses these timestamps to determine the **order** in which transactions should be executed to maintain serializability.

### 3. Optimistic Concurrency Control (OCC):  
  - Transactions are executed **without locking** data during their execution.  
  - Before **committing**, the system checks whether there were **conflicts** with other transactions.  
  - If conflicts are detected, the transaction may be **rolled back**.


### Deadlocks and Prevention

- **Deadlock**:  
  Occurs when **two or more transactions** are blocked because each transaction is **waiting for the other** to release resources.  
  As a result, none of the transactions can proceed.

- **Prevention Techniques**:  
  - **Lock Ordering**:  
    Ensure that all transactions acquire locks in the **same predefined order** to avoid cyclic dependencies.  
  - **Timeouts**:  
    Automatically **roll back** transactions that have been **waiting too long** for resources.


## Backup Types

- **Full Backup**:  
  - Copies the **entire database**, including all data and the database structure.  
  - **Pros**: Simplest to restore.  
  - **Cons**: Takes up a lot of **storage** and **time**.

- **Incremental Backup**:  
  - Copies only the data that has **changed since the last backup** (which may be a full or another incremental backup).  
  - **Pros**: Saves **space** and **time**.  
  - **Cons**: To restore, you need the **full backup + all subsequent incremental backups**.

- **Differential Backup**:  
  - Copies all changes made **since the last full backup**.  
  - **Pros**: Faster than a full backup and **simpler to restore** than incremental backups (requires only the full backup + latest differential).  

- **Transaction Log Backup**:  
  - Copies the **transaction log** of the database.  
  - Allows for **point-in-time recovery**.