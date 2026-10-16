from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD, n = 10**9 + 7, len(nums)
        s, sq, lzy = [0] * (4 * n), [0] * (4 * n), [0] * (4 * n)
        
        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                ln = r - l + 1
                sq[node] = (sq[node] + 2 * v * s[node] + v * v * ln) % MOD
                s[node] = (s[node] + v * ln) % MOD
                lzy[node] = (lzy[node] + v) % MOD
                return
            if lzy[node]:
                lz, mid, left, right = lzy[node], (l + r) // 2, 2 * node, 2 * node + 1
                for ch, ln in ((left, mid - l + 1), (right, r - mid)):
                    sq[ch] = (sq[ch] + 2 * lz * s[ch] + lz * lz * ln) % MOD
                    s[ch] = (s[ch] + lz * ln) % MOD
                    lzy[ch] = (lzy[ch] + lz) % MOD
                lzy[node] = 0
            mid = (l + r) // 2
            if ql <= mid: update(2 * node, l, mid, ql, qr, v)
            if qr > mid: update(2 * node + 1, mid + 1, r, ql, qr, v)
            s[node], sq[node] = (s[2 * node] + s[2 * node + 1]) % MOD, (sq[2 * node] + sq[2 * node + 1]) % MOD

        last, ans = {}, 0
        for r, x in enumerate(nums):
            l = last.get(x, -1) + 1
            last[x] = r
            update(1, 0, n - 1, l, r, 1)
            ans = (ans + sq[1]) % MOD
        return ans