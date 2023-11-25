class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        left, right = 0, sum(nums)

        for i in range(len(nums)):
            right -= nums[i]
            ans.append(right-left + nums[i]*(2*i-n+1))
            left += nums[i]

        return ans
