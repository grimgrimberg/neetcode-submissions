class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0] * n
        # dp[0] = 1
        if n ==1:
            return 1
        
        dp[0] = 1
        dp[1] = 2

        sol = []
        # dp[2] = 2
        #F(n) = F(n-1) + F(n-2)
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
            sol.append(dp[i])
        return dp[n-1]
        