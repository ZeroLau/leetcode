def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        j = sum = 0
        l = k
        for i in range(k):
            sum += nums[i]
        max = sum
        while l < len(nums):
            sum -= nums[j]
            sum+= nums[l]
            j+=1
            l+=1
            if sum >= max:
                max = sum
        return float(max)/k