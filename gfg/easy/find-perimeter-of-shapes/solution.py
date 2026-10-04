class Solution:
    def findPerimeter(self, mat: list[list[int]]) -> int:
        # code here
        n = len(mat)
        m = len(mat[0])
        
        perimeter = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    perimeter += 4
                    
                    if j + 1 < m and mat[i][j + 1] == 1:
                        perimeter -= 2
                        
                    if i + 1 < n and mat[i + 1][j] == 1:
                        perimeter -= 2
                        
        return perimeter