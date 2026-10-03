class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        # code here
        m = 4 * n
        total = 8 * n * n
        
        coila = []
        
        r, c = 0, 0
        
        dir = 0
        
        
        steps = [m - 1]
        for step in range(m -2, 0, -2):
            steps.extend([step, step])
            
        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        
        coila.append(r * m + c + 1)
        
        for step in steps:
            for _ in range(step):
                r += dr[dir]
                c+= dc[dir]
                
                coila.append(r * m + c + 1)
            dir = (dir + 1) % 4
            
        max_val = m * m + 1
        coilb = [max_val - val for val in coila]
        
        return [coila, coilb]