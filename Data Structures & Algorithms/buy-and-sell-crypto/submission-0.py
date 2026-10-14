class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        temp = float('inf')

        for i in prices:
            temp = min(temp, i)
            profit = max(profit, i - temp)

        return profit    