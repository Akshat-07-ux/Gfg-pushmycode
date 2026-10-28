class Solution:
    def solve(self, bt):
        # code here
        bt.sort()
        total_wait = 0
        current_wait = 0
        
        for t in bt:
            total_wait += current_wait
            current_wait += t
            
        return total_wait // len(bt)