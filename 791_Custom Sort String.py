class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        ans = ''
        for char in order:
            if char in s_dict:
                ans += char * s_dict[char]
        
        for char in s:
            if char not in order:
                ans += char
        
        return ans