import math
from typing import List
class Solution:
    def maxLength(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            c_g = 0
            c_l = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                c_g = math.gcd(c_g, x)
                c_l = math.lcm(c_l, x)

                if prod == c_l * c_g:
                    ans = max(ans, j - i + 1)

        return ans



        