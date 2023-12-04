class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) == 0:
            return ""

        ans = ""
        left = 0

        while left < len(num):
            right = left + 1
            while right < len(num):
                if num[left] != num[right]:
                    break
                elif num[left] == num[right]:
                    if right-left+1 >= 3:
                        if ans == "":
                            ans = 0
                        ans = max(int(num[right]), ans)
                        # left = right +1
                        break
                right += 1
            left += 1

        return str(ans)*3


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        for i in range(len(num)):
            j = i+1
            k = i+2
            if k < len(num) and num[i] == num[j] and num[j] == num[k]:
                if ans == "":
                    ans = num[i:k+1]
                elif int(ans[0]) < int(num[i]):
                    ans = num[i:k+1]
        return ans
