class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return -1

        ans = -1
        right = 0
        for left in range(len(nums)):
            right = left + 1
            while k-nums[left] >= 0 and right < len(nums):
                if nums[left] + nums[right] > ans and nums[left] + nums[right] < k:
                    ans = nums[left] + nums[right]
                right += 1

        return ans

# sort


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        ans = -1

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                ans = max(ans, nums[l] + nums[r])
                l += 1
            else:
                r -= 1

        return ans
