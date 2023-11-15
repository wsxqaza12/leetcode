class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        extra = 0

        for i in range(len(flowerbed)-1):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                extra += 1
                flowerbed[i] = 1
            elif flowerbed[i-1] != 1 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                extra += 1
                flowerbed[i] = 1
            elif i == (len(flowerbed)-2) and flowerbed[i] != 1 and flowerbed[i+1] == 0:
                extra += 1

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            extra += 1

        if extra >= n:
            return True
        else:
            return False

### 2 #######################################################


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        fl = [0] + flowerbed + [0]

        for i in range(1, len(fl)-1):
            if fl[i-1] != 1 and fl[i] == 0 and fl[i+1] != 1:
                fl[i] = 1
                n -= 1

        return n <= 0
