class Solution(object):
    def isAnagram(self, s, t):
        set_s = set(s)
        set_t = set(t)

        if len(s) != len(t):
            return False

        if (len(set_s - set_t) == 0 and len(set_t - set_s) == 0):
            for letter in set_s:
                if s.count(letter) != t.count(letter):
                    return False
            return True
        else:
            return False

# 速度較慢


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [str(x) for x in s]
        t_list = [str(x) for x in t]
        s_list.sort()
        t_list.sort()

        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                return False
        return True

# 字典


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = defaultdict(int)
        t_d = defaultdict(int)
        for x in s:
            s_d[x] += 1
        for x in t:
            t_d[x] += 1

        if s_d == t_d:
            return True
        else:
            return False
