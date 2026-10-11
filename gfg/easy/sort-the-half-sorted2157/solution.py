class Solution:
    def mergeTwoParts(self, arr):
        # code here
        n = len(arr)
        
        idx = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                idx = i + 1
                break
            
        if idx == 0:
            return 
            
        temp = [0] * n
        i, j, k = 0, idx, 0
        
        while i < idx and j < n:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
                
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
            
        while i < idx:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j < n:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        arr[:] = temp