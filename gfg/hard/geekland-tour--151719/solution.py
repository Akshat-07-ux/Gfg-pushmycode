from collections import deque
class Solution:
    def maxCities(self, loc: list[int], roads: list[list[int]], k: int) -> int:
        # code here
        
        n = len(loc)
        adj = [[] for _ in range(n + 1)]
        
        for u, v in roads:
            if abs(loc[u - 1] - loc[v - 1]) <= k:
                adj[u].append(v)
                adj[v].append(u)
                
        seen = [False] * (n + 1)
        best = 1
        
        
        def bfs_f(start: int) -> tuple[int, int]:
            dist = {start: 0}
            q = deque([start])
            far_node = start
            while q:
                cur = q.popleft()
                if dist[cur] > dist[far_node]:
                    far_node = cur
                    
                for nxt in adj[cur]:
                    if nxt not in dist:
                        dist[nxt] = dist[cur] + 1
                        q.append(nxt)
            return far_node, dist[far_node]
            
        for i in range(1, n + 1):
            if seen[i]:
                continue
            
            u, _ = bfs_f(i)
            v, diameter = bfs_f(u)
            best = max(best, diameter + 1)
            
            q = deque([u])
            seen[u] = True
            while q:
                cur = q.popleft()
                for nxt in adj[cur]:
                    if not seen[nxt]:
                        seen[nxt] = True
                        q.append(nxt)
                        
        return best