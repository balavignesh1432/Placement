# LRU Cache implementation using Doubly Linked List and HashMap
# Each node in the doubly linked list contains key, value, prev and next pointers
# The front of the list represents the least recently used item
# The rear of the list represents the most recently used item
# The hashmap stores key to node mapping for O(1) access
# When a key is accessed or updated, the corresponding node is removed from the position,
# and moved to the rear
# When adding a new key node is added in rear, size is incremented
# If capacity is exceeded, the front node is removed, and size is decremented
# IMP: Remove from hashmap when evicting the least recently used item
# Time: O(1) for get and put operations
# Space: O(capacity) for the cache and linked list
# Implementation Hacks:
# 1. Use a dummy front and rear node instead of just pointers to simplify add and remove operations
# 2. Use functions to encapsulate node removal, addition to rear, and popping front node logic
# 3. IMP:Need key in Node to delete from hashmap when evicting
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.front = Node(None, None)
        self.rear = Node(None, None) 
        self.cache = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            value = node.val
            if self.size == 1:
                return value
            else: 
                self.remove_node(node)
                self.append_last(node)
                return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            if self.size == 1:
                return
            else:
                self.remove_node(node)
                self.append_last(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            if self.size == 0:
                node.prev = self.front
                node.next = self.rear
                self.front.next = node
                self.rear.prev = node
            else:
                self.append_last(node)
            self.size += 1
            if self.size > self.capacity:
                self.pop_front()
                self.size -= 1

    def remove_node(self, node):
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre

    def append_last(self, node):
        last = self.rear.prev
        last.next = node
        node.prev = last
        node.next = self.rear
        self.rear.prev = node
    
    def pop_front(self):
        front = self.front.next
        del self.cache[front.key]       # Delete from hashmap, key is needed in Node
        new = front.next
        new.prev = self.front
        self.front.next = new


# Alternative implementation using OrderedDict
# OrderedDict maintains the order of insertion
# When a key is accessed or updated, we move it to the end to mark it as recently used
# When adding a new key, if capacity is exceeded, we pop the first item (least recently used)
# Time: O(1) for get and put operations
# Space: O(capacity) for the cache
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)                 # move to end to mark as recently used O(1)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)             # move to end to mark as recently used O(1)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)          # pops the first item (least recently used) O(1)