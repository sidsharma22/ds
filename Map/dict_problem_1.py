################################################################
# Leet Code: https://leetcode.com/problems/running-sum-of-1d-array/
# DS: Dictonary
# Problem Number: 1
################################################################
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1,len(nums)):
            sums[i] = sums[i-1] + nums[i]
            
        return sums
