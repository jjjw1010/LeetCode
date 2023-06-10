class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {} #Map # Key is element Value is index

        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in ind:
                return [ind[comp],i]

            ind[nums[i]] = i 
