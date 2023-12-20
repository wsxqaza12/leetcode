class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        num = 0
        money2 = money
        for price in prices:
            if money >= price:
                money -= price
                num += 1

            if num == 2:
                return money
        return money2
    
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        if prices[0]+prices[1] > money:
            return money
        else:
            return money-prices[0]-prices[1]