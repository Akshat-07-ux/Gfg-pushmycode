class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        
        n = len(s)
        arr = list(s)
        
        left, right = 0, n - 1
        while left < right:
            if arr[left] != '?' and arr[right] != '?':
                if arr[left] != arr[right]:
                    return -1
                    
            elif arr[left] != '?':
                arr[right] = arr[left]
            elif arr[right] != '?':
                arr[left] = arr[right]
            left += 1
            right -= 1
            
        prev_char = None
        for i in range(n // 2):
            if arr[i] != '?':
                prev_char = arr[i]
            elif prev_char is not None:
                arr[i] = prev_char
                arr[n - 1 - i] = prev_char
                
        prev_char = None
        for i in range(n // 2 - 1, -1, -1):
            if arr[i] != '?':
                prev_char = arr[i]
            elif prev_char is not None:
                arr[i] = prev_char
                arr[n - 1 - i] = prev_char
                
        for i in range(n):
            if arr[i] == '?':
                arr[i] = 'a'
                arr[n - 1 - i] = 'a'
                
        total_sum = 0
        for i in range(n - 1):
            total_sum += abs(ord(arr[i]) - ord(arr[i + 1]))
            
        return total_sum
