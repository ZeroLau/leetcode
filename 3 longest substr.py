def lengthOfLongestSubstring(self, s):
    longest = 0
    s = list(s)
    a =[]
    for l in s:
        
        if l in a:
            a.append(l)
            if len(a) > longest:
                longest = len(a)-1
            head = a.index(l)
            i= 0
            while i <= head:
                a.pop(0)
                i+=1
        else:
            a.append(l)
            if len(a) >= longest:
                longest = len(a)
        

    return longest
print(lengthOfLongestSubstring('', " "))