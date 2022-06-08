
# doubly linked list node
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # left pointer (Least recently used key)
        self.left = Node(0,0)
        # right pointer (most recently used key)
        self.right = Node(0,0)
        # initally pointing to each other
        self.left.next = self.right
        self.right.prev = self.left
        
    # removes the given node from the linked list  
    def remove_node(self,node):
        prev = node.prev
        _next = node.next
        prev.next = _next
        _next.prev = prev
    
    # insert the node pointing to the right pointer
    def insert_node_right(self,node):
        prev = self.right.prev
        _next = self.right
        prev.next = node
        _next.prev = node
        node.prev = prev
        node.next = _next
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # before returing update the right pointer where key being the most recent fetched
            # remove the node pointing to the key
            self.remove_node(self.cache[key])
            # insert the node at pointing to right
            self.insert_node_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key already exists in cache
        if key in self.cache:
            # remove the node from list
            self.remove_node(self.cache[key])
        
        # create a new node 
        node = Node(key,value)
        # update cahce by pointing the node
        self.cache[key] = node
        # point the most recently created node to right
        self.insert_node_right(node)
        
        # check if the capacity excceds
        # if it does remove the lru from list and delete from hashmap(cache)
        if len(self.cache) > self.cap:
            # lru node (using left pointer)
            lru = self.left.next
            # remove from ll
            self.remove_node(lru)
            # delete from cache
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)