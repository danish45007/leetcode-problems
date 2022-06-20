'''
892 · Alien Dictionary
Algorithms
Hard
Accepted Rate
27%

DescriptionSolutionNotesDiscussLeaderboard
Description
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


You may assume all letters are in lowercase.
The dictionary is invalid, if string a is prefix of string b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order.
The letters in one string are of the same rank by default and are sorted in Human dictionary order.
Example
Example 1:

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
Example 2:

Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

'''


from typing import (
    List,
)

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        if not words:
            return ""
        if len(set(words)) == 1:
            return "".join(words[0])
        
        adj_list = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            word1,word2 = words[i],words[i+1]
            min_len = min(len(word1),len(word2))
            # check if word2 is prefix of word1
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                   adj_list[word1[j]].add(word2[j])
                   break
        print(adj_list)
        # perform post-order dfs
        visited = {} #{char:state} state -> False(not visited) and True in path
        res = []
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for edge in adj_list[char]:
                if dfs(edge):
                    return True
            visited[char] = False
            res.append(char)
        for c in sorted(adj_list.keys(),reverse=True):
            if dfs(c):
                return ""
        res.reverse()
        return ''.join(res)

