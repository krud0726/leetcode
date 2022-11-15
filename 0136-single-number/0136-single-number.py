from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        answer = [k for k,v in c.items() if v == 1]
        print(answer)
        
        return answer[0]
    
    
    def singleNumber(self, nums: List[int]) -> int:
        c = {}
        
        for n in nums:
            if n in c:
                c[n] = c[n] + 1
            else:
                c[n] = 1
        print(c)
        
        for k,v in c.items():
            if v == 1:
                return k
        