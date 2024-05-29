def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        l = [0]
        for i in range(len(gain)):
            l.append(l[i]+gain[i])
        return max(l)
