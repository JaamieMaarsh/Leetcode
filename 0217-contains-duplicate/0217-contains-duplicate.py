class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict()
        
        for i, num in enumerate(nums):
            if num in hashmap:
                return True
            else:
                hashmap[num] = i
        return False