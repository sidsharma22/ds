################################################################
# Leet Code: https://leetcode.com/problems/set-mismatch/
# DS: Hash Table
# Problem Number: 3
################################################################

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map = {nums[0]:0}
        given_set = set(nums)
        ideal_set = set(list(range(1,len(nums)+1)))
        lost_element =  list(ideal_set - given_set)[0]## [2,1,3] -- [2,2]
        
        for i in range (1, len(nums)):
            if (nums[i]) in map:
                repeated_element = nums[i]
                return [repeated_element, lost_element]
            else:
                map[nums[i]] = i
        return [0,0]
