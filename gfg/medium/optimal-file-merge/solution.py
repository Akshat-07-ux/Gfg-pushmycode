import heapq
class Solution:
    def minComputation(self, files):
        # code here
        
        if not files:
            return 0
            
            
        heapq.heapify(files)
        total = 0
        
        while len(files) > 1:
            first = heapq.heappop(files)
            second = heapq.heappop(files)
            
            merged = first + second
            total += merged
            
            heapq.heappush(files, merged)
            
        return total
        