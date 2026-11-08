class Solution:
    def wineSelling(self, arr):
        # code here
        tot_wor = 0
        cur_bal = 0
        
        for val in arr:
            cur_bal += val
            tot_wor += abs(cur_bal)
            
        return tot_wor