class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            c = target - n
            
            if c in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(c) + (i+1)]
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
        