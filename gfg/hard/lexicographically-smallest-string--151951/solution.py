class Solution:
    def lexiString(self, s: str) -> str:
        # code here
        l = len(s)
        
        twice = s + s
        i, j, k = 0, 1, 0
        
        while i < l and j < l and k < l:
            y = twice[i + k]
            z = twice[j + k]
            
            if y == z:
                k += 1
                
            elif y > z:
                i += k + 1
                if i <= j:
                    i = j + 1
                k = 0
            else:
                j += k + 1
                if j <= i:
                    j = i + 1
                k = 0
        
        res = min(i, j)
        return twice[res: res + l]