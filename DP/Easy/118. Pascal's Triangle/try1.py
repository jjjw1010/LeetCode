
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]] * numRows
        if numRows == 1:
            return dp
        dp[1] = [1, 1]
        if numRows == 2:
            return dp

        # 3rd row to numRows
        for i in range(2, numRows):
            prev = dp[i-1]
            curr = [1] * (i + 1)
            for j in range(1, len(prev)):
                curr[j] = prev[j-1] + prev[j]
            dp[i] = curr
        return dp
