def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        while num > 0:
            if num %2 == 1:
                num -= 1 
            else:
                num //= 2
            i +=1
        return(i)