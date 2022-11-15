class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        
        counter = {}
        stk = []
        
        for i in s:
            if not counter.get(i,0):
                counter[i] = 0
                
            counter[i] = counter.get(i, 0) + 1
            
        for char in s:
            counter[char] -= 1
            if char in stk:
                continue
            
            while stk and char < stk[-1] and counter[stk[-1]] > 0:
                val = stk.pop()
            
            stk.append(char)
        
        return ''.join(stk)
    
    
    def removeDuplicateLetters(self, s: str) -> str:
        
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        
        return ''
        