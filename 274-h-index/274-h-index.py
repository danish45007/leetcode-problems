class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        l = 0
        r = len(citations)-1
        res = 0
        n = len(citations)
        while l <= r:
            mid = (l+r) // 2
            number_of_citations = n-mid
            if citations[mid] == number_of_citations:
                return citations[mid]
            elif citations[mid] <= number_of_citations:
                l = mid+1
            else:
                r = mid-1
        return n-l
