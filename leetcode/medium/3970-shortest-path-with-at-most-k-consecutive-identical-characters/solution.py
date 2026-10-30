from typing import List
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        
        if n == 1:
            return 0

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {}

        heap = [(0, 0, 1)]
        dist[(0, 1)] = 0

        while heap:
            d, u, count = heapq.heappop(heap)

            if u == n - 1:
                return d

            if d > dist.get((u, count), float('inf')):
                continue

            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    next_count = count + 1

                else:
                    next_count = 1

                if next_count <= k:
                    nd = d + w

                    if nd < dist.get((v, next_count), float('inf')):
                        dist[(v, next_count)] = nd
                        heapq.heappush(heap, (nd, v, next_count))

        return -1
                        