class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = {0:1}
        ans = 0
        cur_sum = 0

        for num in nums:
                cur_sum += num
                ans +=  prefix_sum.get(cur_sum-goal, 0)
                prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1

        return ans

# Time complexity:O(n)
# Space complexity:O(1)