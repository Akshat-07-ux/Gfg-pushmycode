class Solution:
    def count(self, n):
        # code here
        
        total_edges = n * (n - 1) // 2
        return 1 << total_edges