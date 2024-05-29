def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        while prices != [prices[0]]:
            
            testlist = [] + prices
            testlist.sort()
            testlist.reverse()
            if testlist == prices:
                print(prices)
                print(testlist)
                return profit
            
            low = min(prices)
            lowspot = prices.index(low)
            for i in range(lowspot, len(prices)):
                    if prices[i]-low>profit:
                        profit = prices[i]-low
            prices = prices[0:lowspot]
            if prices == []:
                  return profit
        return profit
print(maxProfit("", [6,1,3,2,4,7]))