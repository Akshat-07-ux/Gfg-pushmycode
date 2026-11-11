class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        def cal(x):
            return x * costBoth + max(0, need1 - x) * cost1 + max(0, need2 - x) * cost2

        return min(cal(0), cal(min(need1, need2)), cal(max(need1, need2)))