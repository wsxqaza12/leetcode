class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        right = 0

        for left in range(len(nums)-1):
            right = left+1
            while right < len(nums):
                if nums[left] == nums[right]:
                    count += 1
                    right += 1
                else:
                    break

        return count
