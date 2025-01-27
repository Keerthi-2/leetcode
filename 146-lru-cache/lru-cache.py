class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}  # This will store the nodes (key: node)
        self.head = None  # Initially head is None
        self.tail = None  # Initially tail is None

    # Add node to the front (newly added, most recent)
    def add(self, node):
        if not self.head:
            # If the list is empty, set both head and tail to this node
            self.head = node
            self.tail = node
        else:
            # Otherwise, add it to the front (after head)
            node.next = self.head
            self.head.prev = node
            self.head = node

    # Remove a node from the doubly linked list
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        node.prev = node.next = None

    def get(self, key):
       
        if key in self.cache:
            node = self.cache[key]
            # Remove the node from its current position
            self.remove(node)
            # Add it to the front (most recent)
            #print("hi")
            self.add(node)
            return node.val
        return -1

    def put(self, key, value):
        #print(self.cache)
        if key in self.cache:
            # Remove the old node for this key
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            
            # Cache is full, remove the least recently used (tail)
            del self.cache[self.tail.key]
            self.remove(self.tail)
            

        # Create a new node and add it as the most recent one
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)