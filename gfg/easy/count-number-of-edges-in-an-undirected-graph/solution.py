class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        # code here
        total = 0
        for neighbours in adj:
            total += len(neighbours)
            
        return total // 2
        
