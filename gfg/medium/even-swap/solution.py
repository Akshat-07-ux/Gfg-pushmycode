class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        if n <= 1:
            return arr
            
        res = list(arr)
        i = 0
        
        while i < n:
            j = i
            
            while j < n and (res[j] % 2 == res[i] % 2):
                j += 1
                
            res[i:j] = sorted(res[i:j], reverse=True)
            i = j
            
        return res