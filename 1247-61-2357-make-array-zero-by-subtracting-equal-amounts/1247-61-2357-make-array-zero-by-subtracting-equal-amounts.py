class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        i=0
        while i<len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:     
                i+=1   
        total_operations = len(set(nums))
        return total_operations 
        