def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(" ")
        l.reverse()
        #print(l)
        d = ""
        i = 1
        for i in range(len(l)):
            if l[i]!= "":
                d += l[i]+" "
        return d[:-1]