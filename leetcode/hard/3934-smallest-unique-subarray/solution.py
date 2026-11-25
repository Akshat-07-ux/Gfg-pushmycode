from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        mod, base = (1 << 61) - 1, 1315423911
        pw = [1] * (n + 1)
        hs = [0] * (n + 1)

        for i, x in enumerate(nums):
            pw[i + 1] = pw[i] * base % mod
            hs[i + 1] = (hs[i] * base + x + 1) % mod

        def has_unique(k: int) -> bool:
            unique = set()
            dups = set()
            mul = pw[k]

            for i in range(n - k + 1):
                h = (hs[i + k] - hs[i] * mul) % mod

                if h in dups:
                    continue
                if h in unique:
                    unique.remove(h)
                    dups.add(h)
                else:
                    unique.add(h)
            return bool(unique)

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo