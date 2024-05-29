def gcdOfStrings(self, str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    tempstr = ""
    if len(str2) > len(str1):
        str1, str2 = str2, str1
    for i in range(len(str2), 0, -1):
        tempstr = str2[:i]
        if tempstr * (len(str1)//len(tempstr)) == str1 and tempstr * (len(str2)//len(tempstr)) == str2:
            print(tempstr)
    print("")
    return tempstr
gcdOfStrings("", "ABABAB", "ABAB")