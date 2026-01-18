class Node:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node: Node):
        prev, next = self.tail.prev, self.tail
        prev.next, next.prev = node, node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

# Get() and put() run in O(1) time
# Intuition: use a hashmap to store key-value pairs (key: node). This lets us store the addresses of nodes which we can access in O(1) time.
# To handle the LRU part, use a doubly linked list with dummy nodes for the head and tail. 
# If we go over the capacity, remove the LRU (given by the start of the linked list) and also from the cache.
# Otherwise, if we use get() or put() remove the node and reinsert it at the end of the linked list so that its the "most recently used".