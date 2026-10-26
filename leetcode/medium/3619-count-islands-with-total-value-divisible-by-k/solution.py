class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    current_sum = 0
                    stack = [(r, c)]

                    current_sum += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        curr_r, curr_c = stack.pop()

                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                            nr, nc = curr_r + dr, curr_c + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                current_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if current_sum % k == 0:
                        count += 1
        return count   