import sys
sys.setrecursionlimit(2000000)
class Solution:
    def checkIfSubtree(self, n, edges, queries):
        # code here
        
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        in_time = [0] * (n + 1)
        out_time = [0] * (n + 1)
        timer = 0
        
        def dfs(u, p):
            nonlocal timer
            timer += 1
            in_time[u] = timer
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
                    
            timer += 1
            out_time[u] = timer
            
        dfs(1, 0)
        
        result = []
        for a, b in queries:
            if in_time[b] <= in_time[a] <= out_time[b]:
                result.append(True)
            else:
                result.append(False)
                
        return result
        