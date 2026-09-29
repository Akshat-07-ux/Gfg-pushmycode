class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        zx, zy = 1, 1
        
        for val in arr:
            if val == x:
                zx += 1
                
            elif val == y:
                zy += 1
                
        if zx > zy:
            return x
            
        elif zy > zx:
            return y
            
        else:
            return min(x, y)