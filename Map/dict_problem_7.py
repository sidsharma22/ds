################################################################
# Leet Code: https://leetcode.com/problems/word-pattern
# DS: Dictonary
# Problem Number: 7
################################################################
#---------------------------------------------------------------
#  1. Convert the input strings into list  
#  2. Create 2 dictonaries
#  3. Exit the function if the pattern length is not equal to the input string list.
#  4. Traverse through pattern list and store the occurance of each letter in a dictonary.
#  5. Traverse through string list and store the occurance of each word in a dictonary.
#  6. Check if the occurance of each key in dictonary_1 matches in dictonary_2.
#---------------------------------------------------------------


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_list = s.split()
        pattern_l = list(pattern)
        map_1 = {}
        map_2 = {}
        if len(pattern_l) != len(str_list):
            return False
        else:
            for i in range(len(pattern_l)):
                if pattern_l[i] in map_1:
                    map_1[pattern_l[i]] = map_1[pattern_l[i]] + [i]
                else:
                    map_1[pattern_l[i]] = [i]
            for i in range(len(str_list)):
                if str_list[i] in map_2:
                    map_2[str_list[i]] = map_2[str_list[i]] +[i]
                else:
                    map_2[str_list[i]] = [i]
            for i in range(len(pattern_l)):
                    if map_1[pattern_l[i]] != map_2[str_list[i]]:
                        return False
            return True
