def isPalindrome(self, x):
    """
        :type x: int
        :rtype: bool
        """
    num = x
    rev = 0
    while num>0:
        rev = rev*10 + num%10
        num= num//10
    print(rev)
    return True if x == 0 or rev/x == 1 else False
print(isPalindrome("", 1122))