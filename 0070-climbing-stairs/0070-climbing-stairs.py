"""
꼭대기까지 오르는데 사용될 수 있는 경우의 수 구하기
i => i번째 계단

D[i] => i번째 계단을 오르는데 드는 경우의 수 = D[i] = D[i-1] + D[i-2]
D[2] = D[1] + D[0]
i-2 = 
i-1 = 
"""

class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs1(self, n: int) -> int:
        dp = [0] * (46)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
    def climbStairs2(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        