class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])
        pivot = 0
        if right == 0:
            return 0

        while pivot < len(nums)-1:
            left = left + nums[pivot]
            right = right - nums[pivot+1]
            pivot += 1
            if left == right:
                return pivot
        return -1
