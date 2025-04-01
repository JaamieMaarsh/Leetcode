class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(log N) - binary search

        # 1) sort in ascending -> 2) binary search - O(NlogN) - but this wont work since the index of the rotated array is required.

        l=0
        r=len(nums)-1
        # [4,5,6,7,0,1,2]
        while l<=r:
            mid = (l+r) // 2 # mid = 3

            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]: # array is sorted on the left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            else: # nums[r] > nums[mid]: # array is sorted on the right
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
                
        
     
      

        


