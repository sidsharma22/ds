################################################################
# Leet Code: https://leetcode.com/problems/reshape-the-matrix/
# DS: Array
# Problem Number: 4
################################################################
#---------------------------------------------------------------
### Complexity: O(2*nums)
### Algorithm 
#  1. Covert 2d to 1d
#  2. See if len of array is equal to r*c
#  3. Pick elements from 1d array to reshape
#---------------------------------------------------------------
class Solution:

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        array= []
        prime = [2]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                array.append(nums[i][j])
        print(array)
        print(len(array))
        
        l1 = []
        if len(array) == r*c:
            for i in range(r):
                l1.append([])
                for j in range(c):
                    print(j+i*r)
                    l1[i].append(array[j+i*c])
        else: return nums
        return l1
