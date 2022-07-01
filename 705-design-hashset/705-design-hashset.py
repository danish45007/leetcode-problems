class MyHashSet:

    def __init__(self):
        self.look_up_table_size = 10**6
        self.look_up_table = [None]*self.look_up_table_size #[bucket1,bucket2....]
        
    def get_hash_value(self,key):
        return key%self.look_up_table_size
            
    def add(self, key: int) -> None:
        hash_value = self.get_hash_value(key)
        # check if its the first addition of key
        if not self.look_up_table[hash_value]:
            # creating a new bucket
            self.look_up_table[hash_value] = [key]
        else:
            self.look_up_table[hash_value].append(key)
            

    def remove(self, key: int) -> None:
        hash_value = self.get_hash_value(key)
        if self.look_up_table[hash_value]:
            while key in self.look_up_table[hash_value]:
                self.look_up_table[hash_value].remove(key)
        

    def contains(self, key: int) -> bool:
        hash_value = self.get_hash_value(key)
        if not self.look_up_table[hash_value]:
            return False
        else:
            if key in self.look_up_table[hash_value]:
                return True
            else:
                return False
            
            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)