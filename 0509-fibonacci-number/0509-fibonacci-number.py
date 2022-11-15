class Solution:
    def fib1(self, n: int) -> int:
        if n <= 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)
    
    
    def fib2(self, n: int) -> int:
        dp = collections.defaultdict(int)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
    
    # 3. Memoization
    def fib3(self, n: int) -> int:
        dp = collections.defaultdict(int)
        
        if n <= 1:
            return n
        
        if dp[n]:
            return dp[n]
        
        dp[n] = self.fib(n-1) + self.fib(n-2)
        return dp[n]
    
    
    # 4. Using two variables for memory saving
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
            print("x : ", x, " y : ", y)
            
        return x
        