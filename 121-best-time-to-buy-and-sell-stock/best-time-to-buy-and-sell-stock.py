class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
     
        
        minprice=prices[0]
        maxprofit=0
        for i in prices[1:]:
            profit=i-minprice
            maxprofit=max(maxprofit,profit)
            minprice=min(minprice,i)
        return maxprofit