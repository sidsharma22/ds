################################################################
# Leet Code: https://leetcode.com/problems/contains-duplicate-ii/  
# DS: Dictonary
# Problem Number: 6
################################################################
#---------------------------------------------------------------
#  Function: containsNearbyDuplicte 
#  input:   nums - list of numbers 
#           k - integer 
#  Description: Used dictonary find out the if any number in the list repeats within the given integer range.
#---------------------------------------------------------------
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_1 = {}
        for i in range(len(nums)):
            if nums[i] in map_1:
                diff = abs(map_1[nums[i]] - i)
                if diff <= k: return True
            map_1[nums[i]] = i
        return False 
