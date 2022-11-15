from itertools import combinations

class Solution:
    # 문제에 적합한 비교 함수
    @ staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1)+str(n2) < str(n2) + str(n1)
    
    
    # 삽입 정렬 구현
    def largestNumber1(self, nums: List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str,nums))))
        
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x))
        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int(''.join(nums[::-1])))
        