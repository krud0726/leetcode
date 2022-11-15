class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if len(nums) < 3:
            return answer
        
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
            
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        print("answer : ", answer)
        return answer
        