import math
class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        
        l = len(arr)
        leaf = [0] * (4 * l)
        
        def make(node, start, end):
            if start == end:
                leaf[node] = arr[start]
                return 
        
            mid = (start + end) // 2
            make(2 * node, start, mid)
            make(2 * node + 1, mid + 1, end)
            leaf[node] = math.gcd(leaf[2 * node], leaf[2 * node + 1])
        
        def makeone(node, start, end, ind, val):
            if start == end:
                leaf[node] = val
                return
            
            
            mid = (start + end) // 2
            if start <= ind <= mid:
                makeone(2 * node, start, mid, ind, val)
                
            else:
                makeone(2 * node + 1, mid + 1, end, ind, val)
                
            leaf[node] = math.gcd(leaf[2 * node], leaf[2 * node + 1])
            
        def doubt(node, start, end, l, r):
            if r < start or end < l:
                return 0
                
                
            if l <= start and end <= r:
                return leaf[node]
                
            mid = (start + end) // 2
            
            return math.gcd(
                doubt(2 * node, start, mid, l, r),
                doubt(2 * node + 1, mid + 1, end, l, r)
                )
                
        make(1, 0, l - 1)
        
        win = []
        for q in queries:
            if q[0] == 0:
                win.append(doubt(1, 0, l -1, q[1], q[2]))
                
            else:
                ind, val = q[1], q[2]
                arr[ind] = val
                makeone(1, 0, l - 1, ind, val)
                
        return win
                
                
        
        