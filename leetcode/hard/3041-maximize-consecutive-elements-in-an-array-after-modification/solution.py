class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        nums.sort()
        ans = 0
        dp = {}


        for x in nums:
            nxt = dp.get(x, 0) + 1
            if nxt > dp.get(x + 1, 0):
                dp[x + 1] = nxt
                ans = max(ans, nxt)

            cur = dp.get(x - 1, 0) + 1
            if cur > dp.get(x, 0):
                dp[x] = cur
                ans = max(ans, cur)

        return ans