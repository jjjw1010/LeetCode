class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex + 1
        dp = [[1] * (i+1) for i in range(n)]
        for j in range(2, n):
            for k in range(1, len(dp[j-1])):
                dp[j][k] = dp[j-1][k-1] + dp[j-1][k]
        return dp[rowIndex]
