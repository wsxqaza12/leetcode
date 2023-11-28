class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        diff = list(set(range(0, len(nums)+1)) - set(nums))
        return diff[0]


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] != i:
                return i
        return n
