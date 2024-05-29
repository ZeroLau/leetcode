def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l1.reverse()
    l2.reverse()
    x = "".join(map(str, l1))
    y = "".join(map(str, l2))
    res = int(x) + int(y)
    res = list(str(res))
    res.reverse()
    return res
print(addTwoNumbers("", [2,4,3],[5,6,4]))