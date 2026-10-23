import sys
sys.setrecursionlimit(100000)
class Solution:

    def maxCities(self, roads: list[list[int]], n: int) -> int:
        # code here
        
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
            
        sz = [0] * n
        
        def get_sizes(u, p):
            sz[u] = 1
            for v in adj[u]:
                if v != p:
                    get_sizes(v, u)
                    sz[u] += sz[v]
                    
        get_sizes(0, -1)
        
        min_sum_sq = float('inf')
        
        def evaluate(u, p):
            nonlocal min_sum_sq
            sum_sq = 0
            for v in adj[u]:
                if v != p:
                    sum_sq += sz[v] * sz[v]
                    
            parent_sz = n - sz[u]
            sum_sq += parent_sz * parent_sz
            
            if sum_sq < min_sum_sq:
                min_sum_sq = sum_sq
                
            for v in adj[u]:
                if v != p:
                    evaluate(v, u)
                    
        evaluate(0, -1)
        return ((n - 1) * (n - 1) - min_sum_sq) // 2
        
        
