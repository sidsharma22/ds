################################################################
# Leet Code: https://leetcode.com/problems/two-sum/
# DS: Dictonary
# Problem Number: 2
################################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {target - nums[0]: 0}
        for i in range (1, len(nums)):
            if nums[i] in map:
                return [map[nums[i]],i]
            else:
                map[target - nums[i]] = i
        return [0,0]
