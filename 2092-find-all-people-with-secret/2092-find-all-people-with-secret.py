class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meeting_time_person_map = defaultdict(list)
           
        meetings.sort(key=lambda x:x[2]) # sort meeting based on start time
        for person1,person2,start_time in meetings:
            meeting_time_person_map[start_time].append([person1,person2])
        has_secret = set()
        # adding 0th person and firstPerson into set as they know the secret
        has_secret.add(0)
        has_secret.add(firstPerson)
        for time,persons in meeting_time_person_map.items():
            graph = defaultdict(list)
            seen = set() 
            for person1,person2 in persons:
                graph[person1].append(person2)
                graph[person2].append(person1)
                if person1 in has_secret:
                    seen.add(person1)
                if person2 in has_secret:
                    seen.add(person2)

            queue = deque(seen)
            while queue:
                person = queue.popleft()
                for neighbour in graph[person]:
                    if neighbour not in has_secret:
                        has_secret.add(neighbour)
                        queue.append(neighbour)
        return has_secret
                    
        
        
        
                
        
            