class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Base Case
        # 1 1 1 1 1 n = 1
        # 5 4 3 2 1 n = 2 (15)
        # 15 10 6 3 1 n = 3 (30)

        dp = [[1] * 5] * n
        for i in range(1, n):
            for j in range(5):
                dp[i][j] = sum(dp[i-1][j:])
        return sum(dp[n-1])
