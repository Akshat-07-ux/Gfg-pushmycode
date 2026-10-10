class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_k = k1 + k2

        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diffs) <= total_k:
            return 0

        max_val = max(diffs)
        count = [0] * (max_val + 1)
        for d in diffs:
            count[d] += 1

        for i in range(max_val, 0, -1):
            if count[i] > 0:
                if total_k >= count[i]:
                    total_k -= count[i]
                    count[i - 1] += count[i]
                    count[i] = 0

                else:
                    count[i] -= total_k
                    count[i - 1] += total_k
                    total_k = 0
                    break

        ans = 0

        for i in range(1, max_val + 1):
            if count[i] > 0:
                ans += count[i] * (i * i)

        return ans