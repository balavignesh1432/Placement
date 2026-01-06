# API Design

## API Types: REST, GraphQL, gRPC

For real-time features like notifications, chat, or live updates, you'll need different protocols like **WebSockets** or **Server-Sent Events**. These aren't traditional APIs — they're persistent connections.

---

## REST

### Resources Are Core Entities

REST resources should represent **things** in your system, not actions.

**Key Rule:** Resources should always be **plural nouns**.

---

### Nested Resources (Parent-Child)

Use **path parameters** when the value is required. If the relationship is always required for the query to make sense, use a path parameter.

```
/events/{id}/tickets
```

---

### Flat Resources

Use **query parameters** when the filter is optional.

```
/tickets?event_id=123&section=VIP
```

Query parameters work well for **pagination**.

---

### Request Body

Data you're sending to create or update resources. The request body is where you put complex data structures and anything that might be too large or sensitive for a URL.

---

### HTTP Methods and Idempotency

**Idempotency:** Operations that can be safely repeated without changing the outcome.

| Method | Safe | Idempotent | Purpose |
|--------|------|-----------|---------|
| **GET** | ✅ | ✅ | Retrieve resource |
| **POST** | ❌ | ❌ | Create resource (calling multiple times creates multiple) |
| **PUT** | ❌ | ✅ | Replace entire resource |
| **PATCH** | ❌ | ✅ | Update part of resource |
| **DELETE** | ❌ | ✅ | Remove resource |

---

### API Response

**Status Code:**
- `2xx` — Success
- `4xx` — Client errors
- `5xx` — Server errors

**Response Body:** The actual data returned.

---

## GraphQL

### Core Concept

The client specifies the **shape of the response**, and the server returns data in that exact format.

**Design Approach:**
Instead of REST's resource endpoints, you design a **schema** that defines your data types and their relationships.

---

### Complexity Trade-offs

GraphQL adds complexity. You need to implement:
- Query parsing
- Schema validation
- Sophisticated caching strategies

---

### The N+1 Problem: The Biggest GraphQL Gotcha

**Scenario:**
- Query returns 100 events
- For each event, you need to fetch its venue
- Result: 100 queries for venues + 1 initial query = **101 database queries**

Without optimization, this is wasteful.

**Solution: Batching/DataLoader**

Instead of multiple queries:
```sql
SELECT * FROM venue WHERE id = 1
SELECT * FROM venue WHERE id = 2
```

Combine into one:
```sql
SELECT * FROM venue WHERE id IN (1, 2, 3, ...)
```

**Note:** Batching adds complexity you don't have with REST.

---

## RPC — Remote Procedure Call

### Core Concept

Unlike REST's resource-oriented approach, RPC is **action-oriented**. You're calling functions across a network as if they were local functions in your codebase.

**Comparison:**
```
REST:  GET /events/123
RPC:   getEvent(eventId: "123")
```

---

### gRPC: Google Remote Procedure Call

**Technology Stack:**
- Uses **Protocol Buffers** for serialization
- Uses **HTTP/2** for transport

**How It Works:**

1. Write a `.proto` file that describes service methods and data structures

```protobuf
service TicketService {
  rpc GetEvent(GetEventRequest) returns (Event);
}

message GetEventRequest {
  string event_id = 1;
}

message Event {
  string id = 1;
  string name = 2;
}
```

2. gRPC generates client and server code in **multiple programming languages**

---

### When to Use gRPC

- Internal service communication
- Polyglot environments (different services in different languages)

---

## API Patterns

### Pagination

Two main strategies: **offset-based** and **cursor-based**.

---

#### Offset-Based Pagination

**Format:**
```
/events?offset=20&limit=10
```

**How It Works:**
- Specify how many records to skip (`offset`)
- Specify how many to return (`limit`)

**Problem:**
If someone adds a new event while you're paginating through results, you might see **duplicates or miss records** as the data shifts.

---

#### Cursor-Based Pagination

Uses a **pointer to a specific record** instead of counting from the beginning.

**First Request:**
```
/events?limit=10
```

**Response includes:**
- The events
- A cursor pointing to the last record

**Next Request:**
```
/events?cursor=cmd9atj3p000007ky19w1dpy2&limit=10
```

**How It Works:**
- The cursor is typically an **encoded reference** to a specific record (like an ID or timestamp)
- More stable because it's not affected by new records being added

**Trade-off:**
- Harder to implement features like "jump to page 5"

---

### Versioning

**Purpose:** Handle changes without breaking existing clients.

---

#### URL Versioning

Include the version number in the path:

```
/v1/events
/v2/events
```

**Advantages:**
- Clients know exactly which version they're using just by looking at the URL
- Simple to implement since you can route different versions to different code paths

---

#### Header Versioning

Put the version in an HTTP header:

```
Accept-Version: v2
API-Version: 2
```

**Disadvantages:**
- Less obvious to developers
- Harder to test in browsers

---

## Security

### Authentication vs Authorization

**Authentication:**
Verifies **identity** — proving the user is who they claim to be.

**Authorization:**
Verifies **permissions** — checking if that authenticated user is allowed to perform the specific action they're requesting.

**Implementation:** Enable **Role-Based Access Control (RBAC)**.

---

### API Keys

**What They Are:**
Long, randomly generated strings that act like passwords for applications.

**How They Work:**

1. Generate an API key for each client
2. Store it in your database along with permissions and rate limits
3. Verify each incoming request by looking up the key

**Use Cases:**
- Perfect for server-to-server communication where you control both sides

**Limitations:**
- API keys don't expire

---

### JWT — JSON Web Tokens

**Core Idea:**
Encode user information directly into the token itself rather than storing session state on your server.

**How It Works:**

1. User logs in successfully
2. Server creates a **JWT** containing:
   - User ID
   - Permissions
   - Expiration time
3. Server **signs** the entire token with a secret key
4. JWT comes back with future requests
5. Server verifies authenticity by checking the signature
6. User information is read directly from token (no database lookup needed)

**Example JWT Payload:**
```json
{
  "user_id": "123",
  "email": "john@example.com",
  "role": "customer",
  "exp": 1640995200
}
```

**Advantages:**
- Stateless (no database lookup required)
- Can carry user context
- Ideal for user-facing applications

---

### Rate Limiting

**Purpose:**
Prevent abuse by restricting how many requests a client can make in a given time period. Protects your system from malicious attacks and accidental overuse.

**Examples:**

| Type | Limit |
|------|-------|
| **Per-user limits** | 1000 requests per hour per authenticated user |
| **Per-IP limits** | 100 requests per hour for unauthenticated requests |
| **Endpoint-specific limits** | 10 booking attempts per minute |

**Implementation:**
- Typically implement at the **API gateway level** or using **middleware** in your application