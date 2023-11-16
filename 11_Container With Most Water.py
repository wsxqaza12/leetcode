class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxwater = 0

        while left != right:
            min_height = min(height[left], height[right])
            if min_height * (right-left) > maxwater:
                maxwater = min_height * (right-left)

            if min_height == height[left]:
                left += 1
            else:
                right -= 1

        return maxwater
