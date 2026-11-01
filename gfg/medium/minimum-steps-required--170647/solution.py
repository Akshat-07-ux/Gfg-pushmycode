class Solution:
    def minSteps(self, str: str) -> int:
        # code here
        
        if not str:
            return 0
            
        blocks = 1
        
        for i in range(1, len(str)):
            if str[i] != str[i - 1]:
                blocks += 1
                
        return (blocks // 2) + 1