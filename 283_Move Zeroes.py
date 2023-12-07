class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        curr = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[curr] = nums[i]
                curr += 1

        for _ in range(count):
            nums[curr] = 0
            curr += 1

        return nums

#


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[no_zero] = nums[no_zero], nums[i]
                no_zero += 1

        return nums
