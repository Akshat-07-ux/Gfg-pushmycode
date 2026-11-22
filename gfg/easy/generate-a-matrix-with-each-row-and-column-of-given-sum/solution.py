class Solution:
    def generateMatrix(self, rowSum, colSum):
        # code here
        
        n, m = len(rowSum), len(colSum)
        grid = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                val = min(rowSum[i], colSum[j])
                grid[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
        
        return grid 