class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result =[]

        #edge cases
        if len(nums)<3:
            return []

        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i-1] and i>0: # checking duplicates for the 'a' value
                continue
            a = nums[i] #outer value
            l = i+1
            r = len(nums)-1
            while l<r:
                sum = nums[i]+nums[l]+nums[r]
                if sum == 0: 
                    result.append([nums[i],nums[l],nums[r]])
                    #to check for next combination
                    l += 1
                    r -=1
                    # check for duplicate keys
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
                    while nums[r] == nums[r+1] and l<r:
                        r -=1    
                elif sum <0:
                    l += 1
                    # check for duplicate keys
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
                elif sum >0:
                    r -=1
                    while nums[r] == nums[r+1] and l<r:
                        r -=1 
        return result

