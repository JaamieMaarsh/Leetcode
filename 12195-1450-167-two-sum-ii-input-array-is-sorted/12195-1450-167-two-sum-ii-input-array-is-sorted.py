class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1] # l,r return the index as it starts from 1 and the position is +1 from index 
            if sum > target:
                r -= 1
            else:
                l +=1
        return [l+1,r+1]
            