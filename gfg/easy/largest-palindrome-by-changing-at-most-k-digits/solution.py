class Solution:
    def maxPalindrome(self, s: str, k: int) -> str:
        # code here
        a = list(s)
        n = len(a)
        mod = [0] * n
        
        for i in range(n // 2):
            j = n - 1 - i
            if a[i] != a[j]:
                m = max(a[i], a[j])
                a[i] = a[j] = m
                mod[i if a[i] == m else j] = 1
                
                k -= 1
                
        if k < 0:
            return "-1"
            
        for i in range(n // 2):
            j = n - 1 - i
            if a[i] < "9":
                need = 2 - mod[i] - mod[j]
                
                if k >= need:
                    a[i] = a[j] = "9"
                    k -= need
                    
                    
        if n % 2 and k:
            a[n // 2] = "9"
            
        return "".join(a)