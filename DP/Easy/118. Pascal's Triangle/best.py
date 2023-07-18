class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Init for Memoization
        dp = [[1] * i for i in range(1, numRows + 1)]

        # Base Case are Row1 and Row2
        for i in range(2, numRows):
            for j in range(1, len(dp[i-1])):
                # Relation to Subproblems
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp
