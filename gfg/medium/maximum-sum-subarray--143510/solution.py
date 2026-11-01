class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        """ code here """
        
        
        no_square = arr[0]
        one_square = arr[0] * arr[0]
        
        max_sum = max(no_square, one_square)
        
        
        for i in range(1, len(arr)):
            prev_no_square = no_square
            prev_one_square = one_square
            
            no_square = max(arr[i], prev_no_square + arr[i])
            
            one_square = max(
                arr[i] * arr[i],
                prev_no_square + arr[i] * arr[i],
                prev_one_square + arr[i]
            )
            
            max_sum = max(max_sum, no_square, one_square)
            
        return max_sum