class Solution:
    def countPaths(self, edges):
        # code here
        
        
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        children = [[] for _ in range(n)]
            
        visited = [False] * n
        queue = [0]
        visited[0] = True
            
        idx = 0
        while idx < len(queue):
            curr = queue[idx]
            idx += 1
            for nxt in adj[curr]:
                if not visited[nxt]:
                    visited[nxt] = True
                    children[curr].append(nxt)
                    queue.append(nxt)
                        
        ans = [0] * n
            
        def dfs(curr, balance):
            count = 0
            if balance == 0:
                count += 1
                    
            for nxt in children[curr]:
                nb = balance + (1 if nxt % 2 == 1 else -1)
                count += dfs(nxt, nb)
                    
            return count
                 
        for i in range(n):
            init_balance = 1 if i % 2 == 1 else -1
            ans[i] = dfs(i, init_balance)
                
        return ans