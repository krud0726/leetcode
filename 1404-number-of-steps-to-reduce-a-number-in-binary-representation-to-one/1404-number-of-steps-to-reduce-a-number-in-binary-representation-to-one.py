class Solution:
    def numSteps(self, s: str) -> int:
        val = int(s,2)
        
        i = 0
        while val > 1:
            if val % 2 == 0:
                val //= 2
            else:
                val += 1
                
            i += 1
            
        return i