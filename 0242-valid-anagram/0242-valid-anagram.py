class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        # t가 s의 애너그램인지 확인
        
        for i, v in enumerate(t):
            print(i,v)
            if v in s:
                s = s.replace(v, '0', 1)
            else:
                s += '*'
            
        return -s.isdigit()
    
    
    def isAnagram(self, s: str, t: str) -> bool:
        # t가 s의 애너그램인지 확인
        
        return sorted(s) == sorted(t)
        