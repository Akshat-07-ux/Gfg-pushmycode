import heapq
class Solution:
    def minTime(self, grid):
        # code here
        
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        visited = [[False]* n for _ in range(n)]
        visited[0][0] = True
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c = heapq.heappop(pq)
            
            if r == n - 1 and c == n - 1:
                return t
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))
                    
        return 0