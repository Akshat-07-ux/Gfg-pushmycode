class Solution:

    def countPopulation(self, n: int) -> int:
        """code here"""
        
        births = [0] * (n + 1)
        births[1] = 1
        active = 1
        
        for day in range(2, n + 1):
            if day - 6 >= 1:
                active -= births[day - 6]
                
            new_born = active * 2
            births[day] = new_born
            active += new_born
            
        return active