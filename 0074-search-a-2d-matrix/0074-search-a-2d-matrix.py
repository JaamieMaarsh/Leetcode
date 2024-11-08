class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # dimensions of matrix
        row = len(matrix)
        col = len(matrix[0])
        
        # Initial pointers for binary search over rows
        top_row = 0
        bottom_row = row - 1

        # Find the correct row where the target might be
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            # Check if target might be in this row
            if target < matrix[middle_row][0]:  # Check if target is less than the first element of the middle row
                bottom_row = middle_row - 1
            elif target > matrix[middle_row][-1]:  # Check if target is greater than the last element of the middle row
                top_row = middle_row + 1
            else:
                # Target must be in this row
                break

        # If no valid row is found
        if not (top_row <= bottom_row):
            return False

        # Perform binary search on the identified row
        middle_row = (top_row + bottom_row) // 2
        l, r = 0, col - 1  # Column pointers for binary search within the row
        while l <= r:
            m = (l + r) // 2
            if target > matrix[middle_row][m]:
                l = m + 1
            elif target < matrix[middle_row][m]:
                r = m - 1
            else:
                return True  # Target found

        return False  # Target not found


        
