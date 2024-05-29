def longestCommonPrefix(self, strs):
    """
        :type strs: List[str]
        :rtype: str
        """
    if strs == []:
        return False
    short = 100
    for a in range(len(strs)):
        if strs[a] == "":
            return ""
        elif len(strs[a]) <= short:
            short = len(strs[a])
            b = a
    s = strs[b]
    end = ""
    for i in range(len(s)):
        p = 0
        for j in range(len(strs)):
            k = strs[j]
            if s[i] != k[i]:
                p = 1
        if p == 0:
            end +=s[i]
        else:
            return end
    return end
print(longestCommonPrefix("", ["cir","car"]))