class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rev = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                rev = max(r, sell - buy)
        return rev 