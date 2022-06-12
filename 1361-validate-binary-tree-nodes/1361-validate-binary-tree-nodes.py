class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # step: #1 (building tree)
        parent_to_child_map = defaultdict(list) #{parent:[child1,child2]}
        child_to_parent_map = {} # child : parent
        for node in range(n):
            left_child = leftChild[node]
            right_child = rightChild[node]
            
            if left_child != -1:
                parent_to_child_map[node].append(left_child)
                # check for multple parent
                if left_child not in child_to_parent_map:
                    child_to_parent_map[left_child] = node
                else:
                    return False
            
            if right_child != -1:
                parent_to_child_map[node].append(right_child)
                # check for multple parent
                if right_child not in child_to_parent_map:
                    child_to_parent_map[right_child] = node
                else:
                    return False
        
        # checking for multiple roots
        root_node = None
        for node in range(n):
            if node not in child_to_parent_map:
                if not root_node:
                    root_node = node
                else:
                    return False
        if root_node == None:
            return False
        
        visited = set()
        queue = deque()
        queue.append(root_node)
        # check if the tree does not form a cycle
        while queue:
            curr_node = queue.popleft()
            visited.add(curr_node)
            for child in parent_to_child_map[curr_node]:
                queue.append(child)
        return len(visited) == n
                
                
        