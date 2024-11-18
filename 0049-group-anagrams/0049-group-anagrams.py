from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None:
            return None
        
        hashmap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26 # creating an array holding the 26 characters
            for c in s:
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())
        