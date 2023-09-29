class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        s = set()
        ans = []

        for first in range(len(nums)):
            for left in range(first+1, len(nums)):
                mid = left + 1
                right = len(nums) - 1

                while mid < right:
                    sum = nums[first] + nums[left] + nums[mid] + nums[right]
                    if sum == target:
                        s.add((nums[first], nums[left],
                              nums[mid], nums[right]))
                        mid += 1
                        right -= 1
                    elif sum < target:
                        mid += 1
                    else:
                        right -= 1

        ans = list(s)
        return ans
