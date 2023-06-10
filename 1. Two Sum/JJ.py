class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            comp = target - nums[i]
            if comp in nums[i + 1 : n]:
                return [i, nums.index(comp, i + 1,n)]
