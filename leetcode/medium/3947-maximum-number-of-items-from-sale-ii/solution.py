class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        mx = max(f for f, _ in items)
        freq = [0] * (mx + 1)
        for f, _ in items:
            freq[f] += 1

        mult = [0] * (mx + 1)
        for d in range(1, mx + 1):
            mult[d] = sum(freq[m] for m in range(d, mx + 1, d))


        opt = []
        for f, p in items:
            if p <= budget:
                free_cap = mult[f] - 1
                if free_cap > 0:
                    opt.append((p / 2, 2, p, min(free_cap, budget // p)))
                opt.append((p, 1, p, budget // p))

        opt.sort()
        total = 0
        for _, gain, p, cap in opt:
            take = min(cap, budget // p)
            total += take * gain
            budget -= take * p

        return total


        