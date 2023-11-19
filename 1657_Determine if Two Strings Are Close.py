class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for x in word1:
            m1[x] += 1
        for x in word2:
            m2[x] += 1

        m1v = sorted(list(m1.values()))
        m2v = sorted(list(m2.values()))

        if m1v != m2v:
            return False
        elif set(m1.keys()) != set(m2.keys()):
            return False
        else:
            return True
