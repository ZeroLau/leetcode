def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    r= len(nums)-1
    l=0
    while l<r:
        if nums[l] + nums[r] == target:
            return [l,r]
        if l == r-1:
            r-=1
            l=0
        else:
            l+= 1
print(twoSum("", [3,2,4], 6))