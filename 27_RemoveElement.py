class Solution(object):
    def removeElement(self, nums, val):
        slow = 0
        fast = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
