class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """m=0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                m=max(prices[j]-prices[i],m)
        return m"""
        l=0
        profit=0
        for r in range(1, len(prices)):
            if prices[r]<prices[l]:
                l=r
            elif prices[r]-prices[l]>profit:
                profit = prices[r]-prices[l]
        return profit