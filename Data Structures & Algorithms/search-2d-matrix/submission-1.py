class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        top, bottom = 0, m - 1
        row = -1  # initialize

        # Step 1: find correct row
        while top <= bottom:
            mid = (top + bottom) // 2
            
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                row = mid
                break

        # ❗ if no valid row found
        if row == -1:
            return False

        # Step 2: binary search in row
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False