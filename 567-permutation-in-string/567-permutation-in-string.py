class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left,right = 0,0
        char_count_map = {}
        for char in s1:
            char_count_map[char] = 1 + char_count_map.get(char,0)
        window_size = len(s1)
        count = len(char_count_map)
        
        while right < len(s2):
            if s2[right] in char_count_map:
                char_count_map[s2[right]] -=1
                if char_count_map[s2[right]] == 0:
                    count -= 1
                # once reached the window
            if right-left+1 == window_size:
                if count == 0:
                    return True

                # time to move the left pointer to right and mantain the window size
                if s2[left] in char_count_map:
                    # increment the count of left char as the window is moving right
                    char_count_map[s2[left]] +=1
                    # inc. the count as s2[left] has been added into hashmap for the first time
                    if char_count_map[s2[left]] == 1:
                        count +=1
                left +=1
            right +=1
        return False
                            
                        
            
        