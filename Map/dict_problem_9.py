################################################################
# Leet Code: https://leetcode.com/problems/group-anagrams
# DS: Dictonary
# Problem Number: 9
################################################################
#---------------------------------------------------------------
#  1. Sort each element in the list
#  2. Use the sorted element as the key for map/hash table m1
#  3. Store all the elements same as sorted key in a list pointed to by the key.
#  4. Store the values of the map in a list and return the list
#---------------------------------------------------------------
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m1 = {}
        l1 = []
        if strs == [[""]]:
            return [[""]]
        else:
            for i in strs:
                m = ''.join(sorted(i))
                if m in m1:
                    m1[m] = m1[m] +[i]
                else:
                    m1[m] = [i]
            for k in m1:
                l1.append(m1[k])
            return l1
