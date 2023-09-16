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