class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        top_row = 0
        bottom_row = row -1

        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row)//2
            if target < matrix[middle_row][0]:
                # the target is present in the above row
                bottom_row = middle_row - 1
            elif target > matrix[middle_row][-1]:
                top_row = middle_row + 1
            else: # the element is in the middle row
                l = 0
                r = column - 1
                

                while l<=r:
                    m = (l+r)//2
                    if target == matrix[middle_row][m]:
                        return True
                    elif target < matrix[middle_row][m]:
                        r = m-1
                    else:
                        l = m+1
                return False
        return False
                    

                