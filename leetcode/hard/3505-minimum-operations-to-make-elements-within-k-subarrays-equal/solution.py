from typing import List
from heapq import heappush, heappop

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        left, right = [], []
        delayed = {}
        size_l = size_r = 0
        sum_l = sum_r = 0

        def prune(heap):
            while heap:
                v = -heap[0] if heap is left else heap[0]
                if delayed.get(v, 0):
                    heappop(heap)
                    delayed[v] -= 1
                    if delayed[v] == 0:
                        del delayed[v]
                else:
                    break

        def balance():
            nonlocal size_l, size_r, sum_l, sum_r

            if size_l > size_r + 1:
                prune(left)
                v = -heappop(left)
                size_l -= 1
                sum_l -= v
                heappush(right, v)
                size_r += 1
                sum_r += v

            elif size_l < size_r:
                prune(right)
                v = heappop(right)
                size_r -= 1
                sum_r -= v
                heappush(left, -v)
                size_l += 1
                sum_l += v

        def add(v):
            nonlocal size_l, size_r, sum_l, sum_r

            prune(left)

            if not left or v <= -left[0]:
                heappush(left, -v)
                size_l += 1
                sum_l += v
            else:
                heappush(right, v)
                size_r += 1
                sum_r += v

            balance()

        def remove(v):
            nonlocal size_l, size_r, sum_l, sum_r

            prune(left)
            prune(right)

            delayed[v] = delayed.get(v, 0) + 1

            if v <= -left[0]:
                size_l -= 1
                sum_l -= v
                if v == -left[0]:
                    prune(left)
            else:
                size_r -= 1
                sum_r -= v
                if right and v == right[0]:
                    prune(right)

            balance()

        costs = []

        for i, v in enumerate(nums):
            add(v)

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                prune(left)
                m = -left[0]
                costs.append(m * size_l - sum_l + sum_r - m * size_r)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for j in range(1, k + 1):
            for i in range(x, n + 1):
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i - x][j - 1] + costs[i - x]
                )

        return dp[n][k]