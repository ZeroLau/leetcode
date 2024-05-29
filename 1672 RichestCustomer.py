def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        i = 0
        j = 0
        for a in range(len(accounts)):
            i = 0
            for b in accounts[a]:
                i += b 
            if i >=j:
                j = i
        return j