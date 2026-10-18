class Solution: 
    def adjToMat(self, adj):
        # code here
        
        v = len(adj)
        matrix = [[0] * v for _ in range(v)]
        for i in range(v):
            for j in adj[i]:
                matrix[i][j] = 1
        return matrix