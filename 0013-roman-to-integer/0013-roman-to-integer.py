class Solution:
    def romanToInt(self, s: str) -> int:
        
        # creating the hashmap
        roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
        value = 0
        
        for i in range(len(s)): # gives the index from the string s
            if i+1 < len(s) and roman_values[s[i+1]] > roman_values[s[i]]:
                value -= roman_values[s[i]]
            else:
                value += roman_values[s[i]]
        return value
                
            