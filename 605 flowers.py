def canPlaceFlowers(self, flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    beds = 0
    count = 1
    for bed in flowerbed:
        if bed:
            count = 0
        else:
            count +=1
            if count == 3:
                beds += 1
                count -= 2
    if not flowerbed[-1] :
        count += 1
        if count == 3:
            beds += 1
    return beds >= n
print(canPlaceFlowers("", [0,0,0,1], 1))