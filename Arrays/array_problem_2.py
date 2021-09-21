################################################################
# Leet Code: https://leetcode.com/problems/number-of-good-pairs/
# DS: Array
# Problem Number: 2
################################################################
#---------------------------------------------------------------
### Solution
#  Complexity: N^2
#  1. Compare all one element with all the greater index elemnets. 
#  2. If the number is identical increase the count 
#  3. Return Count 
#---------------------------------------------------------------
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count = count +1
        return count 

#######################
# Solution 2: Nlog(N)
#######################
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq  = 0
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                freq =  freq  + 1
            else:
                print(freq)
                count = int(count + (freq*(freq+1))/2)
                freq = 0
            if i == (len(nums)-2) and freq > 0:
                count = int(count + (freq*(freq+1))/2)                
        return count
