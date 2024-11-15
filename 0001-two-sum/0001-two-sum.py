class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict()
        
        
        for i,num in enumerate(nums):
            difference = target - num
            
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[num] = i
        return None
                
        