class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n = len(nums)
        ans = float('inf')

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                length = j - i + 1

                if length > r:
                    break

                if length >= l and cur > 0:
                    ans = min(ans, cur)

        return ans if ans != float('inf') else -1
        
