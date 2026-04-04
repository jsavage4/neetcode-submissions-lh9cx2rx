class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        minPrice = 101
        for price in prices:
            ret = max(ret, price - minPrice)
            minPrice = min(minPrice, price)
        
        return ret