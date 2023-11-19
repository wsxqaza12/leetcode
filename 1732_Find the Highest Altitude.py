class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr = 0

        for alt in gain:
            curr = curr + alt
            highest = max(highest, curr)

        return highest
