def solve(p,q):
    '''
		Time: O(n)
		Space: O(n)
    '''
    # seen = set()
    # while p:
    #     seen.add(p)
    #     p = p.parent
    
    # while q:
    #     if q in seen:
    #         return q
    #     q = q.parent
    
    
    '''
		Time: O(n)
		Space: O(1)
    '''
    p_copy = p
    q_copy = q
    
    while p_copy != q_copy:
        p_copy = p_copy.parent if p_copy else q
        q_copy = q_copy.parent if q_copy else p
    return p_copy
    