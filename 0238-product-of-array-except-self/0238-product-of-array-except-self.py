class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Product of Prefix and Suffix of the element
        result = [1]*len(nums) #creating an array with same length of nums
        prefix = suffix = 1
        
        # Step 1: Calculating the Prefix
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]
        # Step 2: Calculating the Suffix
        for i in range(len(nums)-1,-1,-1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
        return result