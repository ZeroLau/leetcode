def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = list(magazine)
        l = []
        for i in ransomNote:
            if i in mag:
                mag.remove(i)
                l.append(i)
            else:
                return False
        if len(l) == len(ransomNote):
            return True
        else:
            return False