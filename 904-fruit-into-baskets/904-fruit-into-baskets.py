class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        _max = 0
        i,j = 0,0
        _map = {}
        _max_toys = 2
        if(len(set(fruits)) == 1):
            return len(fruits)
        while j < len(fruits):
            if fruits[j] in _map:
                _map[fruits[j]] +=1
            else:
                _map[fruits[j]] = 1
            
            if len(_map) < _max_toys:
                j +=1
            elif(len(_map) == _max_toys):
                _max = max(_max,(j-i+1))
                j +=1
            else:
                while len(_map) > _max_toys:
                    _map[fruits[i]] -=1
                    if(_map[fruits[i]] == 0):
                        del _map[fruits[i]]
                    i+=1
                j +=1
        
        return _max