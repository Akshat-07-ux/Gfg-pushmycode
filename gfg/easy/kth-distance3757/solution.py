class Solution:
    def checkWithinK(self, arr: list[int], k: int) -> bool:
        # code here
        
        seen = {}
        
        for i, num in enumerate(arr):
            if num in seen and i - seen[num] <= k:
                return True
                
            seen[num] = i
            
        return False