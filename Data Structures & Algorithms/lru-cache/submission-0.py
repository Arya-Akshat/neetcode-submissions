class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.cache = {}
        #make dummy DLL
        self.left = Node(0, 0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right , self.left

    #remove node
    def remove(self, node):
        left = node.prev
        nxt = node.next
        nxt.prev , left.next = left, nxt
    # add node at start
    def add(self, node):
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next =nxt
        nxt.prev = node
      
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache) == self.cap:
                # remove LRU node
                lru = self.right.prev
                self.remove(lru)
                del self.cache[lru.key]

            node = Node(value, key)
            self.cache[key] = node
            self.add(node)

        
