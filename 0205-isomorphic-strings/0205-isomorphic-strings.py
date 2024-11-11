class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            return False
        
        for char in range(len(s)):
            if s[char] not in hashmap_s:
                hashmap_s[s[char]] = char
            
            if t[char] not in hashmap_t:
                hashmap_t[t[char]] = char
                
            if hashmap_s[s[char]] != hashmap_t[t[char]]:
                return False
            
        return True
                
        
        
            