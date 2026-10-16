class Solution:
    def countAlwaysFound(self, arr):
        # code here
        
        n = len(arr)
        if n == 0:
            return 0
            
        left_max = [0] * n
        cur_max = arr[0]
        
        for i, x in enumerate(arr):
            if x > cur_max:
                cur_max = x
            left_max[i] = cur_max
            
        right_min = [0] * n
        cur_min = arr[-1]
        
        for i in range(n-1, -1, -1):
            if arr[i] < cur_min:
                cur_min = arr[i]
                
            right_min[i] = cur_min
            
        valid_count = 0
        for i in range(n):
            ok_left = (i == 0) or (arr[i] > left_max[i - 1])
            ok_right = (i == n - 1) or (arr[i] < right_min[i + 1])
            if ok_left and ok_right:
                valid_count += 1
                
        return valid_count