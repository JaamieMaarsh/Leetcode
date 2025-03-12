class Node:
    def __init__(self, key, value):
        self.key, self.value = key,value
        self.next = None
        self.prev = None # just initialised the node

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # holds key& node

        # left (LRU) and right (most recently used) nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, Node): # near the right pointer

        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = Node
        Node.prev, Node.next = prev, nxt

    def remove(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next = nxt
        nxt.prev = prev

        # Left node -> Node 1 -> Node 2 -> right node
        #   prev            Node     next
        # node.next will be Node 2, Nxt = node.next
        # node.prev will left node, previous = node.prev
        # Now cut the links
        # prev.next = node.next = nxt
        # next.prev = node.prev = previous


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # adds to the rightmost pointer
            return self.cache[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) 
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key] # delete the key from the cache(hash)
        
