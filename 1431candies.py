def kidsWithCandies(self, candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    output = []
    for i in candies:
        if i + extraCandies >= max(candies):
            output.append(True)
        else:
            output.append(False)
    return(output)