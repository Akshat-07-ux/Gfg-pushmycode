class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zero = nums.index(0)
        n = len(nums)

        def check(step: int):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True

        ans = float('inf')

        if check(1):
            ans = min(ans, zero, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2, n - zero)

        return ans if ans != float('inf') else -1