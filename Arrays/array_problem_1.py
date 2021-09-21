################################################################
# Leet Code: https://leetcode.com/problems/non-decreasing-array/
# DS: Array
# Problem Number: 1
################################################################
#---------------------------------------------------------------
### Algorithm 
#  1. Partial Solution - try again
#  2. 
#  3. 
#---------------------------------------------------------------
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        gem = nums[0]
        for i in range(len(nums)-1):
            j = i+1
            if nums[i] > nums[j]:
                count = count +1
                if count > 1: return False
        return True
