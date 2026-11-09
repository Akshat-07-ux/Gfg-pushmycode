from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:

        busy = []
        available = SortedList(range(k))
        counts = [0] * k


        for i, (t, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            idx = available.bisect_left(i % k)
            if idx == len(available):
                idx = 0

            server = available[idx]
            available.remove(server)

            counts[server] += 1
            heapq.heappush(busy, (t + l, server))

        max_requests = max(counts)
        return [i for i, c in enumerate(counts) if c == max_requests]


        