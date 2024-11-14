class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Initialization of hashmaps
        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)
        
        # End conditions
        if len(s) != len(t):
            return False
        
        for i,nums in enumerate(s):
                hashmap_s[nums] +=1
                
        for i,numt in enumerate(t): 
                hashmap_t[numt] +=1
                
        if hashmap_s == hashmap_t:
            return True
        else: 
            return False
                
        