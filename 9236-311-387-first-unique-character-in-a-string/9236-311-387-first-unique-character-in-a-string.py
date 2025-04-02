class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for i, char in enumerate(s):
            hashmap[char] = hashmap.get(char, 0) + 1 # if the char is not in hashmap returns 0, if not the value

        for i, char in enumerate(s):
            if hashmap[char] == 1:
                return i
        return -1