class Solution(object):
    def sortedSquares(self, nums):
        square_nums = [x**2 for x in nums]
        square_nums.sort()
        return square_nums

        