from collections import deque
class Solution:
    def geeksAndWells(self, mat: list[list[str]]) -> list[list[int]]:
        # code here
        
        n, m, q, d = len(mat), len(mat[0]), deque(), {}
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 'W':
                    q.append((r, c));
                    d[(r, c)] = 0
                    
        while q:
            r, c = q.popleft()
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] != 'N' and (nr, nc) not in d:
                    d[(nr, nc)] = d[(r, c)] + 1
                    q.append((nr, nc))
                    
        return [[-1 if mat[r][c] == 'H' and (r, c) not in d else d.get((r, c), 0) * 2 if mat[r][c] == 'H' else 0 for c in range(m)] for r in range(n)]
        