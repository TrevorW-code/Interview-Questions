class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity # int barrier
        self.cache = {} # map key to node

        self.left, self.right = Node(0,0), Node(0,0) # add dummy nodes - left is LRU (will be bumped), right = MRU 
        self.left.next, self.right.prev = self.right, self.left # connect them to each other

    def remove(self, node):
        prev, nxt = node.prev, node.next # get nodes connected at this node through pointers
        prev.next, nxt.prev = nxt, prev # update pointers to skip current node

    def insert(self, node):
        prev, nxt = self.right.prev, self.right # get the two nodes to insert between prev, and next (dummy)
        prev.next = nxt.prev = node # set the two adjacent nodes pointers to new node
        node.next, node.prev = nxt, prev # connect nodes pointers to adjacent nodes

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove the node at the key location. do this so we can add it to top of "queue"
            self.insert(self.cache[key]) # add node back with key, this time at top of queue
            return self.cache[key].val # return value stored in node
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # create node, register with hash map
        self.insert(self.cache[key]) # add node registered from cache

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru) # remove node just right of the dummy left node
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
