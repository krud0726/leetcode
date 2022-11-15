class Solution:    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        answer = []
        m = 1

        for i in range(len(nums)):
            answer.append(m)
            m = m*nums[i]
            
        m = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= m
            m *= nums[j]
            
        return answer
    
class Solution:
    def productExceptSelf1(self, nums):
        answer = [1]*len(nums)
        f = 1
        e = 1
        for i in range(len(nums)):
            # prefix product from one end
            answer[i] *= f
            f *= nums[i]
            
            # suffix product from other end
            answer[-1-i] *= e
            e *= nums[-1-i]
            
        return answer
    
    
class Solution:
    def productExceptSelf(self, nums):
        prod, zero_cnt = reduce(lambda a, b: a*(b if b else 1), nums, 1), nums.count(0)
        if zero_cnt > 1: return [0]*len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: nums[i] = 0 if c else prod
            else: nums[i] = prod // c
        return nums
        