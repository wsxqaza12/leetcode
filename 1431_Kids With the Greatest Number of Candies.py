class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        threshold = max(candies)
        ans = []

        for i in range(len(candies)):
            if candies[i]+extraCandies >= threshold:
                ans.append(True)
            else:
                ans.append(False)
        return ans
