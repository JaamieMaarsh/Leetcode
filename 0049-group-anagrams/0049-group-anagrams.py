class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strs:
            sorted_key = "".join(sorted(s)) # sorting the current entity for my key in hashmap
            
            if sorted_key not in hashmap: 
                hashmap[sorted_key] = [s] # hashmap[key] = [value] set as alist according to the problem
            else:
                hashmap[sorted_key].append(s) # append the current value to the key 
                
        
        return list(hashmap.values()) # return only the values of the hashmap