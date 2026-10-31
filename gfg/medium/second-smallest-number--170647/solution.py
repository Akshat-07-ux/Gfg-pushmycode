class Solution:

    def secondSmallest(self, a: int, b: int) -> str:
        """ code here """
        
        if b == 1 or a <= 1 or a >= 9 * b:
            return "-1"
            
        s, temp_a = ['0'] * b, a - 1
        
        for i in range(b - 1, 0, -1):
            d = min(9, temp_a)
            s[i], temp_a = str(d), temp_a - d
            
        s[0] = str(temp_a + 1)
        
        i = b - 1
        while i > 0 and s[i] == '9':
            i -= 1
            
        if i == b - 1:
            if s[i] == '0': return "-1"
                
            s[i], s[i - 1] = str(int(s[i]) - 1), str(int(s[i - 1]) + 1)
            
        else:
            i += 1
            s[i], s[i - 1] = str(int(s[i]) - 1), str(int(s[i - 1]) + 1)
            
        return "".join(s)
