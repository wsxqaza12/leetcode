class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = {}
        cur = 0

        for num in arr:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

            if d[num] > len(arr)*.25:
                return num
