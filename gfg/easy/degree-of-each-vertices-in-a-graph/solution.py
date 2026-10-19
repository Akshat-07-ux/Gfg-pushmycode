class Solution:
    def findInOutDegree(self, V, edges):
        # code here
        
        in_deg = [0] * V
        out_deg = [0] * V
        
        for u, v in edges:
            out_deg[u] += 1
            in_deg[v] += 1
            
        return [[in_deg[i], out_deg[i]] for i in range(V)]
