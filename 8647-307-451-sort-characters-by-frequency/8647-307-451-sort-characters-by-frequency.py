class Solution:
    def frequencySort(self, s: str) -> str:
        # introduce a hashmap with a counter
        #  sort by descending order

        hashmap = defaultdict(int)
        array_ans = []

        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        sorted_map = sorted(hashmap.items(), key=lambda item:item[1], reverse=True)
        
        for chars,frequency in sorted_map:
            array_ans.append(chars*frequency)

        
        return "".join(array_ans)