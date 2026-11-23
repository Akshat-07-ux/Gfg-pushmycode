class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        
        lens = [len(s)]
        step = 0
        
        while lens[-1] < pos:
            step += 1
            lens.append(2 * lens[-1] + step)
            
        for i in range(step, 0, -1):
            prev = lens[i - 1]
            if pos <= prev:
                continue
            
            if pos <= prev + i:
                return "$"
                
            offset = pos - (prev + i)
            pos = prev - offset + 1
            
        return s[pos - 1]