class Solution:
    def rotateclockwise(self, arr, k):
        # code here
        
        n = len(arr)
        k %= n
        if k == 0:
            return arr
            
        def flip(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                
                left += 1
                right -= 1
                
        flip(0, n - 1)
        flip(0, k - 1)
        flip(k, n - 1)
        return arr
        
