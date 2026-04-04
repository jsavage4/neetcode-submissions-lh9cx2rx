class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101

        for i in range(len(prices)):
            price = prices[i]
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)
        
        return maxProfit