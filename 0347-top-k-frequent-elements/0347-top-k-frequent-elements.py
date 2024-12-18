# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashmap = defaultdict( )
        
#         for key in nums:
#             if key not in hashmap:
#                 count_value = 1
                
#             else:
#                 count_value += 1
                
#             hashmap[key] = count_value
#             sorted_keys = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)

# # Step 2: Pick the top k keys
# #top_k_keys = sorted_keys[:k]
#         return list(sorted_keys.keys())

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies using a defaultdict
        hashmap = defaultdict(int)
        for key in nums:
            hashmap[key] += 1  # Increment frequency
        
        # Step 2: Sort the keys by their frequency in descending order
        sorted_keys = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)
        
        # Step 3: Return the top k keys
        return sorted_keys[:k]
