from collections import Counter
class Solution:
    def cntValid(self, w: list[int]) -> int:
        # code here
        p = list(range(len(w)))
        
        def find(i):
            while p[i] != i:
                p[i] = p[p[i]]
                
                i = p[i]
            return i
            
        for b in range(31):
            first = -1
            for i, x in enumerate(w):
                if (x >> b) & 1:
                    if first < 0:
                        first = i
                    else:
                        p[find(first)] = find(i)
                        
        return sum(c * (c - 1) // 2 for c in Counter(find(i) for i in range(len(w))).values())
                        
        