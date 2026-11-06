from typing import List
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda l: l[1])
        indexed_queries = sorted(enumerate(queries), key = lambda q: q[1])

        res = [0] * len(queries)

        counts = [0] * (n + 1)
        active = 0

        left = 0
        right = 0
        m = len(logs)

        for q_idx, q in indexed_queries:
            start = q - x
            end = q

            while right < m and logs[right][1] <= end:
                s_id = logs[right][0]
                if counts[s_id] == 0:
                    active += 1

                counts[s_id] += 1
                right += 1

            while left < right and logs[left][1] < start:
                s_id = logs[left][0]
                counts[s_id] -= 1
                if counts[s_id] == 0:
                    active -= 1

                left += 1

            res[q_idx] = n - active
        return res


        