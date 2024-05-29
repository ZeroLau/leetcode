def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s is None or s == "":
        return ""
    else:
        longest = s[0]
        head = 0
        i = 0
        while head != len(s)-1:
            if i != len(s)-1:
                i += 1
                #print(s[head], s[i])
            if s[head] == s[i]:
                word = s[head:i+1]
                if len(word) >= len(longest) and word == word[::-1]:
                    longest = word

            if i == len(s)-1:
                head += 1
                i = head
    return longest
print(longestPalindrome("", "bbbba"))
