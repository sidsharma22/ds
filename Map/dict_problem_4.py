################################################################
# Leet Code: https://leetcode.com/problems/isomorphic-strings
# DS: Dictonary
# Problem Number: 4
################################################################

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_1={}
        map_2={}
        for i in range(len(s)):
            map_1[s[i]] = map_1.get(s[i],[]) + [i]
            map_2[t[i]] = map_2.get(t[i],[]) + [i]             
            if (map_1[s[i]] != map_2[t[i]]): return False
        return True
