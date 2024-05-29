def romanToInt(self, s):
    """
        :type s: str
        :rtype: int
        """
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    stack = 0
    num = ("ICX")
    num2= ("LVI")
    end = 0
    for i, j in enumerate(s):
        if j in num:
            stack += 1
        end += roman[j]
        if (j == "V" or j == "X") and s[i-1] == "I":
            if j == "X":
                stack -= 1
            end -= roman["I"]*2*stack
            stack = 0
        elif (j == "L" or j == "C") and s[i-1] == "X":
            if j == "C":
                stack -= 1
            end -= roman["X"]*2*stack
            stack = 0
        elif (j == "D" or j == "M") and s[i-1] == "C":
            end -= roman["C"]*2*stack
            stack = 0
        else:
            if j in num2 and s[i-1] in num:
                stack = 0
        print(end, stack)
    return end
print(romanToInt("", "MDCCCLXXXIV"))
        
    