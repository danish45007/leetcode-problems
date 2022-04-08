class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_split,correct_split = current.split(":"),correct.split(":")
        h_current,m_current = int(current_split[0]),int(current_split[1])
        h_correct,m_correct = int(correct_split[0]),int(correct_split[1])
        h_diff = h_correct-h_current
        m_diff = m_correct-m_current
        # in case of correct is smaller than current and to reach has to complete a 24 hr. circle
        if(h_diff < 0):
            h_diff += 24
        # in case of correct min is smaller than current add 60 min to the diff and lower the h_diff as one hour cycle added
        if(m_diff < 0):
            m_diff += 60
            h_diff -=1
        _min = h_diff
        while m_diff >= 15:
            m_diff -= 15
            _min +=1
        while m_diff >= 5:
            m_diff -= 5
            _min +=1
        while m_diff >= 1:
            m_diff -= 1
            _min +=1
        return _min
        
        
        