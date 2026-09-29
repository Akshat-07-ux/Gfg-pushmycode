class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 3 or cols < 3:
            return 0
            
        def is_magic(r, c):
            nums = []
            for i in range(3):
                for j in range(3):
                    nums.append(grid[r + i][c + j])
            
            if sorted(nums) != list(range(1, 10)):
                return False
                
            # Check rows
            if grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15: return False
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15: return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15: return False
            
            # Check columns
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15: return False
            
            # Check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        count = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1
                    
        return count