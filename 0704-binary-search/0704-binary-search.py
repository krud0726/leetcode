class Solution:
    def search3(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
    
    
    def search2(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) //2
            
            if nums[mid] < target:
                left = mid + 1 
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            
        return -1
    
    
    def search(self, nums: List[int], target: int) -> int:
        def b_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return b_search(mid+1, right)
                elif nums[mid] > target:
                    return b_search(left, mid-1)
                else:
                    return mid
            
            else:
                return -1
                
        return b_search(0, len(nums)-1)