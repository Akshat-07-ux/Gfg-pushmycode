class Solution:
    def minWeight(self, edges: list[list[int]], nodes: list[int]) -> int:
        # code here
        
        
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        is_required = [False] * (n + 1)
        for node in nodes:
            is_required[node] = True
            
        root = nodes[0]
        parent = [0] * (n + 1)
        order = []
        
        queue = [root]
        visited = [False] * (n + 1)
        visited[root] = True
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            order.append(curr)
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = curr
                    queue.append(neighbor)
                    
                    
        cnt = [1 if is_required[i] else 0 for i in range(n + 1)]
        total_weight = 0
        
        for curr in reversed(order):
            if curr == root:
                continue
            
            if cnt[curr] > 0:
                total_weight += abs(curr - parent[curr])
                cnt[parent[curr]] += cnt[curr]
                
                
        return total_weight