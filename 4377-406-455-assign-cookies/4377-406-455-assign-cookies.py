class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g) # child
        n = len(s) # cookie
        l = 0 # pointer for child
        r = 0 # pointer for cookie
        count =0
        g.sort()
        s.sort()

        while l<m and r<n:
            if s[r] >= g[l]: # size of cookie is greater than greed, so satisfied
                l += 1
                count += 1
            r += 1
        return count


