def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums)<3:
                return []
        nums.sort()
        l = []
        left = 0
        mid = 1
        right = 2
        while left <mid:
                if nums[left] + nums[mid] + nums[right] == 0:
                        templ = [nums[left], nums[mid], nums[right]]
                        templ.sort()
                        
                        if templ not in l:             
                                l.append(templ)
                                #print(l)
                
                if right >= len(nums)-1:
                        if mid >= len(nums) -2 :
                                if left == len(nums) -3:
                                        break
                                else:
                                        while nums[left] == nums[left+1]:
                                                left += 1
                                        left += 1
                                        mid = left +1
                                        right = left +2
                                        

                        else:
                                
                                while nums[mid] == nums[mid+1]:
                                        mid +=1
                                mid += 1
                                right = mid +1
                else:
                        
                        while nums[right] == nums[right+1]:
                                right += 1
                        right += 1
        return l
 
print(threeSum("", []))
        