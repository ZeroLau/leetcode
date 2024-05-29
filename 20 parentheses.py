def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    end = (")}]")
    temp = []
    if len(s)%2 != 0 or s == "":
        return False
    for i in range(len(s)):
        if s[i] == "(":
            temp.append(")")
        elif s[i] == "{":
            temp.append("}")
        elif s[i] == "[":
            temp.append("]")
        else:
            if s[i] in end and temp == []:
                return False
            elif temp[-1] == s[i]:
                #print(temp)
                #print(temp[-1])
                temp.pop(-1)
                #print(temp)
            
            else:
                return False
    if len(temp) != 0:
        return False
    else:
        return True
print(isValid("", "}{"))