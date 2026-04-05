class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        sell = -float('inf')
        profit = 0
        
        for p in prices:
            buy , sell = min(p, buy) , max(sell ,p - buy )
            profit = max(profit, sell)
        return profit
        
