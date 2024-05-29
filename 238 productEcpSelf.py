def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = len(nums)
        res = [1]*num
        lp = 1
        for i in range(num):
            res[i] *= lp
            lp *= nums[i]
        rp = 1
        for i in range(num-1, -1, -1):
            res[i] *= rp
            rp *= nums[i]
        return res