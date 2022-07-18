class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city_count = {}
        for city1,city2 in paths:
            city_count[city1] = 2 + city_count.get(city1,0)
            city_count[city2] = 1 + city_count.get(city2,0)            
        res = ''
        for city,count in city_count.items():
            if count == 1:
                res += city
        return res