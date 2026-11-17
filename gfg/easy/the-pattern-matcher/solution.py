class Solution:
    def findPattern(self, s):
        # code here
        i, n = 0, len(s)
        
        while i < n:
            if s[i] != 'x':
                return False
                
            x_cnt = 0
            while i < n and s[i] == 'x':
                x_cnt += 1
                i += 1
                
            y_cnt = 0
            while i < n and s[i] == 'y':
                y_cnt += 1
                i += 1
                
            if x_cnt != y_cnt:
                return False
                
        return True