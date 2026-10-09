from collections import deque

class Solution:
    def minDistQueries(self, n: int, query: list[int], edges: list[list[int]]) -> list[int]:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        reds = set()
        ans = []
        min_dist = float('inf')

        for q_node in query:
            if reds:
                q = deque([(q_node, 0)])
                vis = {q_node}
                while q:
                    u, d = q.popleft()
                    if d >= min_dist:
                        break
                    if u in reds:
                        min_dist = d
                        break
                    for v in g[u]:
                        if v not in vis:
                            vis.add(v)
                            q.append((v, d + 1))

                ans.append(min_dist)
            else:
                ans.append(-1)
            reds.add(q_node)

        return ans