class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        pair = 0

        for x in nums:
            m[x] += 1
        for x in nums:
            if m[x] < 1 or m[k-x] < 1 or (x+x == k and m[x] < 2):
                continue
            m[x] -= 1
            m[k-x] -= 1
            pair += 1

        return pair
