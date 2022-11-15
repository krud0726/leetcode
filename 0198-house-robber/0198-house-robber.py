"""
DP --> 집 갯수만큼 만들고
DFS로 구성하면 되나?

DP[i] --> i번째 집에서 출발해서 얻을 수 있는 최대 값
DP[i] = max(DP[i-2],DP[i-3]...) + nums[i] ...
"""

class Solution:
    
    def rob1(self, nums: List[int]) -> int:
        l = len(nums)
        
        dp = [0] * 101
        
        if l <= 1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(2, l):
            dp[i] = max(dp[:i-1:]) + nums[i]
            
            
        return max(dp)
    
    
    
    def rob2(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i-1), _rob(i-2) + nums[i])
        return _rob(len(nums) - 1)
    
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp.popitem()[1]
        