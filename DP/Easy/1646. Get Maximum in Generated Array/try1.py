class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n == 0 or n == 1:
            return n

        dp[0] = 0
        dp[1] = 1
        i = 1
        max_val = dp[1]
        while (2 * i <= n):
            dp[2 * i] = dp[i]
            max_val = max(dp[2*i], max_val)
            if 2 * i + 1 <= n:
                dp[2*i + 1] = dp[i] + dp[i + 1]
                max_val = max(dp[2*i + 1], max_val)
            i += 1
        return max_val
