class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        # code here
        n = len(s)
        
        def can_make_valid(k):
            arr = list(s)
            
            for i in range(k):
                arr[p[i]] = "?"
                
                
            for i in range(n - 1):
                if arr[i] != '?' and arr[i + 1] != '?' and arr[i] == arr[i + 1]:
                    return False
                    
            return True
            
        left, right = 0, n
        result = n
        
        
        while left <= right:
            mid = (left + right) // 2
            if can_make_valid(mid):
                result = mid
                right = mid - 1
                
            else:
                left = mid + 1
                
        return result