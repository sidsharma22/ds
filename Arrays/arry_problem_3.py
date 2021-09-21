################################################################
# Leet Code: https://leetcode.com/problems/pascals-triangle
# DS: Array
# Problem Number: 3
################################################################
#---------------------------------------------------------------
### Complexity: O(N^2)
### Algorithm 
#  1. Num of elements in a kth row (k+1)
#  2. Value of nth element in kth row: k-1[n] + k-1[n-1]
#---------------------------------------------------------------
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        master_list = []
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            master_list = [[1],[1,1]]
            for k in range(2,numRows): 
                n = k 
                master_list.append([1])
                print(master_list)
                print(k)
                print(master_list[k])
                print(master_list[k-1][0])
                for m in range(1,n):
                    print(m)
                    master_list[k].append(master_list[k-1][m] + master_list[k-1][m-1])
                master_list[k].append(1)
            return master_list
