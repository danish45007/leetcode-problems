class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        products.sort()
        l,r = 0,len(products)-1
        for i in range(len(searchWord)):
            char = searchWord[i]
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l +=1
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -=1
            # have the matching prefix
            res.append([])
            matching_words = r-l+1
            for j in range(min(3,matching_words)):
                res[-1].append(products[l+j])
        return res