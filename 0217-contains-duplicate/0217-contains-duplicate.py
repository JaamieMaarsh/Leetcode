class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict()
        
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = i
            else:
                return True
        return False