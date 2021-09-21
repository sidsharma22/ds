################################################################
# Leet Code: https://leetcode.com/problems/powerful-integers  
# DS: Dictonary
# Problem Number: 5
################################################################


import math
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x != 1:
            upper_i = int(math.log(bound,math.e)/(math.log(x,math.e)))
        else:
            upper_i = 1
        if y != 1:
            upper_j = int(math.log(bound,math.e)/(math.log(y,math.e)))
        else:
            upper_j = 1
        sums = []
        for i in range(upper_i+1):
            for j in range(upper_j+1):
                _sum =  x**i + y**j 
                if _sum <= bound and _sum not in sums:
                    sums.append(_sum)
        return sums
