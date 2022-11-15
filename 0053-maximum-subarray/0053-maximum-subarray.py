class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        sums = [-(10**4+1)] * (len(nums) + 1)
        sums[0] = nums[0]
        
        for i in range(1, len(nums)):
            if sums[i-1] > 0:
                sums[i] = nums[i] + sums[i-1]
            else:
                sums[i] = nums[i]
                
        return max(sums)
        
        
    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
            
        return max(nums)
    
    
    
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
            
        return best_sum
        