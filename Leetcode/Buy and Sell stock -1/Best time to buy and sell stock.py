class Solution:
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        mn,profit=prices[0],0
        for i in range(1,len(prices)):
            if prices[i]<mn:
                mn=prices[i]
            else:
                profit=max(prices[i]-mn,profit)
        return profit