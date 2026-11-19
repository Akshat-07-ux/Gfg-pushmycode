class Solution:
    def sortIt(self, arr):
        # code here
        
        odd = sorted([x for x in arr if x % 2 == 1], reverse=True)
        even = sorted([x for x in arr if x % 2 == 0])
        arr[:] = odd + even
        
    
