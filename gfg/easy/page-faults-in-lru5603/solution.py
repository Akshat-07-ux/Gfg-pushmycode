class Solution:
    def pageFaults(self, pages, c):
        # code here
        
        memo = {}
        faults = 0
        
        for p in pages:
            if p in memo:
                del memo[p]
                memo[p] = True
                
            else:
                faults += 1
                if len(memo) == c:
                    oldest_page = next(iter(memo))
                    del memo[oldest_page]
                memo[p] = True
                
        return faults