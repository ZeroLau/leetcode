def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def signFunc(num):
            if num == 0:
                return 0
            elif num >0:
                return 1
            else:
                return -1
        product = nums[0]
        nums.remove(nums[0])
        for n in nums:
            product = product * n
        return signFunc(product)
print(arraySign("", [-1,1,-1,1,-1]))