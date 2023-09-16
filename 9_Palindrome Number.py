class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

        # left = 0
        # right = 0
        # lst = [i for i in str(x)]

        # while right < round(len(lst)/2):
        #     print(left)
        #     print(right)
        #     if lst[left] != lst[len(lst)-right-1]:
        #         return False
        #     left += 1
        #     right += 1
        # return True

                