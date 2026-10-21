class Solution:
    def pathMoreThanK(self, V, edges, k):
        # code here
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        def dfs(u, current_weight):
            if current_weight >= k:
                return True
                
            for v, w in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, current_weight + w):
                        return True
                        
                    visited[v] = False
            return False
            
        visited = [False] * V
        visited[0] = True
        return dfs(0, 0)