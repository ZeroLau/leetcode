def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        smax = max(salary)
        smin = min(salary)
        total = 0
        for i in salary:
            total += i
        return float((total - smin - smax)/(len(salary)-2))
print(average("", [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))
        