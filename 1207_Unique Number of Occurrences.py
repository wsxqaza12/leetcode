class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = defaultdict(int)
        for x in arr:
            m[x] += 1

        if len(m.values()) != len(set(m.values())):
            return False
        return True
