class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l=r=1 # assigning left and right pointers to be 1 since the value in the 0th index will always be unique.
        
        while r<len(nums):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r] # assigning the value of rth index to the l pointer
                r+=1
                l+=1
            else:
                r+=1
        return l