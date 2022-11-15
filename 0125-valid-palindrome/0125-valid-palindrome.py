import re
import collections
import heapq

class Solution:
    def isPalindrome0(self, s: str) -> bool:
        # 자료형 데크로선언
        ss = collections.deque()
        
        for char in s:
            if char.isalnum():
                ss.append(char.lower())
                
        while len(ss) > 1:
            if ss.popleft() != ss.pop():
                return False
            
        return True
        

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        print(s)
        return s == s[::-1]
        