class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_set = set()
        res =0
        l=0

        for i in range(0, len(s)):
            while s[i] in result_set:
                result_set.remove(s[l])
                l +=1
            result_set.add(s[i])
            res = max(res,i-l+1 )
        return res