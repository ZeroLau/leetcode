def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    v=('aeiouAEOIU')
    l=0
    r=len(s)-1
    w=list(s)
    while l<r:
        if w[l] in v and w[r] in v :
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1
        elif w[l] in v:
            r -= 1
        elif w[r] in v:
            l += 1
        else:
            l += 1
            r -= 1

    return "".join(w)

print(reverseVowels("", "hello"))