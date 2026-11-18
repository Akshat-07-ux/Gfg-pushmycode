from bisect import bisect_left
class Solution:

    def reachableCount(self, heights: list[int], jumps: list[int],
                       queries: list[int]) -> list[int]:
        """ code here """
        
        st, ans = [], []
        for i in range(len(heights) - 1, -1, -1):
            while st and heights[st[-1]] <= heights[i]:
                st.pop()
                
            s = min(jumps[i], len(st))
            ans.append(heights[st[-s]] if s else heights[i])
            
            st.append(i)
            
        ans.sort()
        return [len(heights) - bisect_left(ans, q) for q in queries]
        
        
        
