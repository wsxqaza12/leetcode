class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        list = [0, 1]
        if n <= 1:
            return list[n]

        for i in range(n-1):
            list.append(list[i] + list[i+1])
        return list[n]
        