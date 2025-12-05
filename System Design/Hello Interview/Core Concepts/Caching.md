# Caching

Databases store data on disk, Memory sits much closer to the CPU and avoids that entirely.  
The core trade-off is simple. 
Caches make reads faster and reduce load on whatever is behind them.
But they introduce complexity around staleness and invalidation.

Layers:
Browsers cache.  
CDNs cache.  
Applications cache.  
Even databases have built-in caching layers.

---

## External Cache

External cache is a standalone cache service that your application talks to over the network.  
You store frequently accessed data in something like Redis or Memcached — every application server can share the same cache.

Start here, then layer on other caching types such as CDN or client-side caching only if the problem calls for them.

Client -> Server -> Cache -> Server (If Miss) -> DB -> Server and Update Cache -> Client  
Check Cache, If hit return, If miss, Fetch from DB as fallback, Update Cache

---

## CDN (Content Delivery Network)

A CDN is a geographically distributed network of servers that caches content close to users.  
Useful for static Contents (Media).  
Ex: Cloudflare

Flow:
- A user requests an image from your app.
- The request goes to the nearest CDN edge server.
- If the image is cached there, it is returned immediately.
- If not, the CDN fetches it from your origin server, stores it, and returns it.
- Future users in that region get the image instantly from the CDN.

---

## Client-Side Caching

Browser (HTTP cache, localStorage) or mobile app using local memory or on-device storage.  
Avoids unnecessary network calls.  
But you have limited control from the backend. Data can go stale and invalidation is harder.

---

## In-Process Caching

Store them in a cache inside each process (Server).  
But cached data is not shared across servers. Each instance of your application has its own cache. If one instance updates or invalidates a cached value, the others will not know.

Useful for small, frequently accessed values that rarely change. (Ex: Feature Flags)

---

## Cache Architecture / Patterns

## Cache Aside (Lazy Loading):
- Application checks the cache.
- If the data is there, return it.
- If not, fetch from the database, store it in the cache, and return it.

The downside is that a cache miss causes extra latency.

## Write-Through Caching (Sync Write to DB):
- The application writes only to the cache.
- The cache then synchronously writes to the database before returning to the application. The write operation does not complete until both the cache and database are updated.
- Redis itself does not natively support write-through, so you need to code DB write logic.

Tradeoffs:
- Slower writes.
- Can also populate the cache with data that may never be read again.
- If the cache update succeeds but the DB write fails, or vice versa, the systems can end up inconsistent.

Use when reads must always return fresh data and system can tolerate slower writes.

## Write Behind or Write Back Caching (Async Write to DB):
- Application writes and reads from cache.
- The cache batches and writes the data to the DB asynchronously (Flushing) in the background.

Risks:
- If the cache crashes before flushing, you can lose data.
- Can lead to inconsistent state.

Use when you need high write throughput and eventual consistency is acceptable.

## Read-Through Caching:
- Cache acts as a smart proxy.
- Application server never talks to the DB directly.
- On a cache miss, the cache itself fetches from the DB, stores the data, and returns it.

CDNs are a form of read-through cache. When a CDN gets a cache miss, it fetches from your origin server, caches the result, and returns it.

---

## Cache Eviction Policies

- ## LRU (Least Recently Used):  
  LRU evicts the item that has not been accessed for the longest time. (Linked List)  
  It is the default in many systems.

- ## LFU (Least Frequently Used):  
  LFU evicts the item that has been accessed the least. It maintains a counter for each key and removes the one with the lowest frequency.  
  Used when certain keys are consistently popular, like trending videos or top playlists.

- ## TTL (Time To Live):  
  Sets an expiration time for each key and removes entries that are too old. It is often combined with LRU or LFU to balance freshness and memory usage.

---

## Common Caching Problems

## Cache Stampede (Thundering Herd):
- A cache stampede happens when a popular cache entry expires and every request misses the cache and goes straight to the database. (Even if short Window like 1s)  
- Instead of one query, you suddenly have thousands overloading DB.  
- If traffic is high, this spike can overwhelm the database and cause cascading failures.

### How to handle it:
- Request coalescing (single flight): Allow only one request to rebuild the cache while others wait. Most effective.
- Cache warming: Refresh popular keys before they expire. This only helps when using TTL-based expiration.

## Cache Consistency:
- Happens when the cache and DB return different values for the same data.
- Common because most systems read from the cache but write to the database first. That creates a window where the cache still holds stale data.

### How to handle it:
- Cache invalidation on writes: Delete the cache entry after updating DB so it gets repopulated with fresh data.
- Short TTLs: Let slightly stale data live temporarily.
- Accept eventual consistency: For metrics and analytics, a short delay is usually fine.

## Hot Keys:
- A cache entry that receives a huge amount of traffic compared to everything else.
- A single hot key can overload one cache node or one Redis shard and become a bottleneck.

### How to handle it:
- Replicate hot keys: Store the same value on multiple cache nodes and load balance reads across them.
- Add a local fallback cache: Keep extremely hot values in-process to avoid pounding Redis.

---

## Cache Necessities

- Read-heavy workload  
- Expensive queries  
- Latency requirements

---

## Cache Keys

How will you look up cached data?  
- For user profiles, the key might be `user:123:profile`.  
- For trending posts, it could be `trending:posts:global`.

---

## Preferences
- Write-through makes sense when you need strong consistency.  
- Extremely hot keys, mention in-process caching.  
- If dealing with static content like images or videos, mention CDN caching.  
- LRU is the safe default answer. TTL is essential for preventing stale data.