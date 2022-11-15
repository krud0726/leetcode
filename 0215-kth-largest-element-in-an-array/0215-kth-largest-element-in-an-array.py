class Solution:
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        print(nums)
        return nums[k-1]
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap =[]
        answer = 0
        
        for n in nums:
            heappush(heap, -n)
        
        for _ in range(0,k):
            answer = heappop(heap)
        
        return -answer
    
    
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        heapify(nums)
        answer = 0
        
        for _ in range(0,len(nums)-k+1):
            answer = heappop(nums)
        
        return answer
        
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k,nums)[-1]
        