class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        # code here
        r, c = 0, 0
        min_r, max_r = 0, 0
        min_c, max_c = 0, 0
        
        for ch in s:
            if ch == 'L':
                c -= 1
                
            elif ch == 'R':
                c += 1
                
            elif ch == 'D':
                r -= 1
                
            elif ch == 'U':
                r += 1
                
            min_r = min(min_r, r)
            max_r = max(max_r, r)
            min_c = min(min_c, c)
            max_c = max(max_c, c)
            
        row_span = max_r - min_r + 1
        col_span = max_c - min_c + 1
        
        return row_span <= n and col_span <=m