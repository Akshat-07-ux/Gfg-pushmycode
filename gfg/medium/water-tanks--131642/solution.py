class Solution:
    def waterTank(self, tanks, x, w):
        # code here
        total = 0
        step = x + w
        
        for amt in tanks:
            if amt <= x:
                total += amt
                continue
            
            extra = amt - x
            full_moves, rem = divmod(extra, step)
            wasted = full_moves * w + min(rem, w)
            total += amt - wasted
            
        return total
        