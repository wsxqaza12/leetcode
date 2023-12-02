class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        ans = sum(tri)
        if n <= 2:
            return tri[n]

        for i in range(3, n):
            tri.append(ans)
            ans = 2*ans - tri[i-3]

        return ans

# DP


class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        if n <= 2:
            return tri[n]

        for i in range(2, n):
            tri.append(tri[i] + tri[i-1] + tri[i-2])

        return tri[n]
