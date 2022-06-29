class Node:
    
    def __init__(self, key = None, val = 0, frequency = 1):
        self.frequency = frequency
        self.val = val
        self.key = key
        self.prev, self.next = None, None

class DoublyLinkedList:
    
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    # when cache size > capacity, we pop LFU but if there are two then we pop LRU.
    # so we can actually directly pop LRU for that LFU Node List, it would be valid.
    def pop_lfu(self):
        lfu_node, lru_next = self.head.next, self.head.next.next
        self.head.next, lru_next.prev = lru_next, self.head
        return lfu_node
    
    def pop(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
    
    def insert(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = self.tail.prev = node
        node.prev, node.next = tail_prev, self.tail
        
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_adjacency_list = defaultdict(DoublyLinkedList)
        self.least_frequency = 0

    # Common update for node when it's frequency is increased due to Get/Put Operation
    def update_node(self, key):
        node = self.cache[key]
        current_node_list = self.freq_adjacency_list[node.frequency]
        current_node_list.pop(node)
        
        # we update(increment) the least frequency when current frequency was the least frequency and
        # least frequent list was empty , we check in simple way if head points to tail then list it empty
        if node.frequency == self.least_frequency and current_node_list.head.next == current_node_list.tail:
            self.least_frequency += 1
            
        self.cache[key] = Node(key, node.val, node.frequency + 1)
        self.freq_adjacency_list[node.frequency + 1].insert(self.cache[key])
    
    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1

        self.update_node(key)
        return self.cache[key].val
  
    def put(self, key: int, value: int) -> None:
	
        if self.capacity == 0:
            return -1
			
        if key not in self.cache:
		
            if len(self.cache) == self.capacity:
                least_frequency_list = self.freq_adjacency_list[self.least_frequency]
                lfu_node = least_frequency_list.pop_lfu()
                del self.cache[lfu_node.key]
                
            self.least_frequency = 1
            self.cache[key] = Node(key, value, 1)
            self.freq_adjacency_list[1].insert(self.cache[key])
                
        else:
            self.update_node(key)
            self.cache[key].val = value