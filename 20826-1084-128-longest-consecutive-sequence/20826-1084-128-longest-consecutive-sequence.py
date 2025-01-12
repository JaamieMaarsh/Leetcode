class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) # orders and removes duplicates
        # numset = {1, 2, 3, 4, 100, 200}
        longest_seq_count = 0

        for num in numset:
            if (num - 1) not in numset: # iter 1: num-1 =0
                length = 1
                while (num + length) in numset: # checks for the next value
                    length += 1
                longest_seq_count = max(length, longest_seq_count)
        return longest_seq_count
