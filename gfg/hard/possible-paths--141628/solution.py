class Solution:
    def maximumWeight(self, n, edges, queries):
        # code here
        
        edges.sort(key=lambda x: x[2])
        
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])
        
        parent = list(range(n + 1))
        
        size = [1] * (n + 1)
        
        def find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
                
            curr = i
            
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
                
            return root
            
        ans = [0] * len(queries)
        total_paths = 0
        edge_idx = 0
        num_edges = len(edges)
        
        for q_idx, x in indexed_queries:
            while edge_idx < num_edges and edges[edge_idx][2] <= x:
                u, v, w = edges[edge_idx]
                edge_idx += 1
                
                root_u = find(u)
                root_v = find(v)
                
                if root_u != root_v:
                    if size[root_u] < size[root_v]:
                        root_u, root_v = root_v, root_u
                        
                    parent[root_v] = root_u
                    
                    total_paths += size[root_u] * size[root_v]
                    size[root_u] += size[root_v]
                    
            ans[q_idx] = total_paths
        return ans