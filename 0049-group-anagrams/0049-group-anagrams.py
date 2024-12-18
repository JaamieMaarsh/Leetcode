class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strs:
            sorted_key = "".join(sorted(s)) #
            
            if sorted_key not in hashmap:
                hashmap[sorted_key] = [s]
            else:
                hashmap[sorted_key].append(s)
                
        
        return list(hashmap.values())