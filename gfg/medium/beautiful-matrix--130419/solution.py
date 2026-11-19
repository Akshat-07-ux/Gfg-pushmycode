class Solution:
    def minOperation(self, mat: list[list[int]]) -> int:
        # code here
        
        n = len(mat)
        col_s = [sum(mat[r][c] for r in range(n)) for c in range(n)]
        
        best = float("inf")
        for r in range(n):
            ops = 0
            
            for c in range(n):
                val = mat[r][c]
                rest = col_s[c] - val
                ops += abs(val - rest)
                
            if ops < best:
                best = ops
                
        return best