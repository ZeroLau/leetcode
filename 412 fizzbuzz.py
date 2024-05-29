def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(n):
            if (1+i)%3 == 0: 
                if(1+i)%5 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Fizz")
            elif(1+i)%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(1+i))
        return(ans)