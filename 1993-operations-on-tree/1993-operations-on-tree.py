class LockingTree:

    def __init__(self, parent: List[int]):
        self.locked = {i: None for i in range(len(parent))}
        self.children = {i: [] for i in range(len(parent))}
        for i in range(1,len(parent)):
            self.children[parent[i]].append(i)
        self.parent = parent
    
    def lock(self, num: int, user: int) -> bool:
        # already locked by some user
        if self.locked[num]: return False
        self.locked[num] = user
        return True
            

    def unlock(self, num: int, user: int) -> bool:
        # locked by the input user
        if self.locked[num] == user:
            self.locked[num] = None
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # upgrade is possible if thr curr node is not lock
        # parents of curr node is not locked
        # one of thr child for curr node is locked
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            i = self.parent[i]
        # all the parents including curr node has not been locked
        queue = deque()
        is_locked = False
        queue.append(num)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                # get all the children of node
                if self.children[node]:
                    for child in self.children[node]:
                        if self.locked[child]:
                            self.locked[child] = None
                            is_locked = True
                        queue.append(child)
        if is_locked:
            self.locked[num] = user
            return True
        
        
                


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)