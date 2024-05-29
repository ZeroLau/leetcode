def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>=len(t):
            if s != t:
                return False  
            else:
                 return True
            return False
        l = list(t)
        for i in s:
            if i in l:
                l = l[l.index(i)+1:]
            else:
                return False
        return True