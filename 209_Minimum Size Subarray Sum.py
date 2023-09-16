class Solution(object):
    def minSubArrayLen(self, target, nums):
        windowStart = 0
        windowEnd = 0
        windowSum = 0
        min_len = float('inf')

        while windowEnd < len(nums):
            windowSum += nums[windowEnd]

            while windowSum >= target:
                min_len = min(min_len, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

            windowEnd += 1

        return (min_len if min_len != float('inf') else 0)
