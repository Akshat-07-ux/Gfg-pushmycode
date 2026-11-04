class Solution:
    def minOps(self, arr: list[int]) -> int:
        # code here
        
        n = len(arr)
        count = 0
        
        for i in range(n // 2):
            if arr[i] != arr[n - 1 - i]:
                count += 1
                
        return (count + 1) // 2
