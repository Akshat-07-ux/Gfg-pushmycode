class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        X = sorted(set([x for r in rectangles for x in (r[0], r[2])]))
        x_idx = {x: i for i, x in enumerate(X)}
        
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x_idx[x1], x_idx[x2]))
            events.append((y2, -1, x_idx[x1], x_idx[x2]))
        events.sort()
        
        counts = [0] * len(X)
        last_y = ans = 0
        
        for y, typ, i1, i2 in events:
            ans += sum(X[i+1] - X[i] for i in range(len(X)-1) if counts[i] > 0) * (y - last_y)
            for i in range(i1, i2):
                counts[i] += typ
            last_y = y
            
        return ans % (10**9 + 7)