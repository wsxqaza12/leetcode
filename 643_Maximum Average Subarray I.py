class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])
        left = 0

        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[left]
            max_sum = max(max_sum, curr_sum)
            left += 1

        return max_sum/k
