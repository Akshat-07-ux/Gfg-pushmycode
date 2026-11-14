class Solution:
    def maxEqualSum(self, s1: list[int], s2: list[int], s3: list[int]) -> int:
        # code here
        sum1, sum2, sum3 = sum(s1), sum(s2), sum(s3)
        
        i1 = i2 = i3 = 0
        n1, n2,n3 = len(s1), len(s2), len(s3)
        
        while i1 < n1 and i2 < n2 and i3 < n3:
            if sum1 == sum2 == sum3:
                return sum1
                
            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= s1[i1]
                i1 += 1
                
            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= s2[i2]
                i2 += 1
                
            else:
                sum3 -= s3[i3]
                i3 += 1
                
        return 0