class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child_eaten = 0

        for i in range(len(s)):
            if child_eaten >= len(g):
                break
            if s[i] >= g[child_eaten]:
                child_eaten += 1
                
        return child_eaten